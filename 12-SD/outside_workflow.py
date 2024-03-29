from parsl.config import Config
from parsl.channels import LocalChannel
from parsl.providers import SlurmProvider
from parsl.executors import HighThroughputExecutor
from parsl.launchers import SrunLauncher
from parsl.addresses import address_by_hostname


# outside running on UI, snippet, partition, address_by_interface
"""  Each job submitted to the scheduler will request 2 nodes for 10 minutes.
"""
config = Config(
    executors=[
        HighThroughputExecutor(
            label="sd_htex",
            address=address_by_interface("ib0"),
            max_workers=1,  # Set number of workers per node
            provider=SlurmProvider(
                cmd_timeout=60,  # Add extra time for slow scheduler responses
                channel=LocalChannel(),
                nodes_per_block=2,
                init_blocks=1,
                min_blocks=1,
                max_blocks=1,
                partition="normal",  # Replace with partition name
                scheduler_options="#SBATCH -A <YOUR_ALLOCATION>",  # Enter scheduler_options if needed
                # Command to be run before starting a worker, such as:
                # 'module load Anaconda; source activate parsl_env'.
                worker_init="",
                # Ideally we set the walltime to the longest supported walltime.
                walltime="00:10:00",
                launcher=SrunLauncher(),
            ),
        )
    ],
)
