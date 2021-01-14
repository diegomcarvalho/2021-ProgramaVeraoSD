import logging

### PARSL CONFIGURATION
# Inside, pars.env, address_interface, overrides
def workflow_config(name, nodes, cores_per_node=24, interval=30, monitor=False):
    import parsl
    from parsl.config import Config
    from parsl.channels import LocalChannel
    from parsl.launchers import SrunLauncher
    from parsl.providers import LocalProvider
    from parsl.addresses import address_by_interface
    from parsl.executors import HighThroughputExecutor
    from parsl.monitoring.monitoring import MonitoringHub

    parsl.set_stream_logger()
    parsl.set_file_logger('script.output', level=logging.DEBUG)

    logging.info('Configuring Parsl Workflow Infrastructure')

    #Read where datasets are...
    env_str = str()
    with open('parsl.env', 'r') as reader:
        env_str = reader.read()
    
    logging.info(f'Task Environment {env_str}')
    
    mon_hub = MonitoringHub(
            workflow_name=name,
            hub_address=address_by_interface('ib0'),
            hub_port=60001,
            resource_monitoring_enabled=True,
            monitoring_debug=False,
            resource_monitoring_interval=interval,
        ) if monitor else None

    config = Config(
        executors=[
            HighThroughputExecutor(
                label=name,
                # Optional: The network interface on node 0 which compute nodes can communicate with.
                # address=address_by_interface('enp4s0f0' or 'ib0')
                address=address_by_interface('ib0'),
                # one worker per manager / node
                max_workers=cores_per_node,
                provider=LocalProvider(
                    channel=LocalChannel(script_dir='.'),
                    # make sure the nodes_per_block matches the nodes requested in the submit script in the next step
                    nodes_per_block=nodes,
                    # make sure 
                    launcher=SrunLauncher(overrides=f'-c {cores_per_node}'),
                    cmd_timeout=120,
                    init_blocks=1,
                    max_blocks=1,
                    worker_init=env_str,
                ),
            )
        ],
        monitoring=mon_hub,
        strategy=None,
    )

    logging.info('Loading Parsl Config')

    parsl.load(config)
    return