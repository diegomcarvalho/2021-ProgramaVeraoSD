from parsl.providers import SlurmProvider
from parsl.channels import SSHChannel
from parsl.launchers import SrunLauncher

# outside running on a Jupyter Notebook, submit via ssh channel
config = Config(
    executors=[
        IPyParallelExecutor(
            ...
            provider=SlurmProvider(
                'debug',
                channel=SSHChannel(
                    hostname='login.sdumont.lncc.br',
                    username='diego.carvalho',     
                    ...