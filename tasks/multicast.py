from builtins import print



from tasks.tasks import Tasks

from systemd.journal import JournaldLogHandler
import logging
logger = logging.getLogger("multcast-test")
logger.addHandler(JournaldLogHandler())

from utils.ssh import SSH, sshObject


class multicast(Tasks):
    def __init__(self):
        super().__init__()


    def execute(self, args):
        file = "/etc/dtux/env.yml"
        config = self.read_configuration(file)

        sshobjFromYml = config[args.source]

        sshobj = sshObject(sshobjFromYml['ipAddress'], sshobjFromYml['user'], sshobjFromYml['password'])

        scp = SSH(sshobj)
        scp.scp_put(sshobj, "/etc/dtux/env.yml", "/root/diego.txt")
        command = scp.run_command("w")
        print(command)
        logger.warning("Some message: %s", command)
        # scp.sscp()




