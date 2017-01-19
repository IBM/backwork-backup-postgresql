import argparse
import logging
import subprocess
import sys

log = logging.getLogger(__name__)

class MySQLBackup(object):
    """Backup a MySQL database.

    It uses `mysqldump` so it's required to have it installed and added to the
    system's PATH. You can use any of the arguments supported by `mysqldump`.
    Use `mysqldump -h` for more information.
    """
    command = "mysql"

    def __init__(self, args, extra):
        self.args = args
        self.extra = extra

    @classmethod
    def parse_args(cls, subparsers):
        """Create the `mysql` subparser for the `backup` command."""
        mysql_parser = subparsers.add_parser(cls.command, description=cls.__doc__)

        mysql_parser.add_argument("--gzip", action="store_true", required=False,
            help="compress output file (requires gzip to be installed)")

        mysql_parser.add_argument("-o", "--output", required=False,
            help="output file path")

    def backup(self):
        """Backup a MySQL database."""
        output_file = None
        gzip_out = None
        mysqldump_out = None

        if self.args.output:
            log.info("starting mysql backup...")
            output_file = open(self.args.output, 'w')

        if self.args.gzip:
            mysqldump_out = subprocess.PIPE

            if output_file:
                gzip_out = output_file
            else:
                gzip_out = sys.stdout

        else:
            if output_file:
                mysqldump_out = output_file
            else:
                mysqldump_out = sys.stdout

        try:
            mysqldump_cmd = ["mysqldump"] + self.extra
            mysqldump_process = subprocess.Popen(mysqldump_cmd, stdout=mysqldump_out)

            if self.args.gzip:
                gzip_process = subprocess.Popen(["gzip"], stdin=mysqldump_process.stdout, stdout=gzip_out)
                mysqldump_process.stdout.close()

            if self.args.output:
                log.info("mysql backup complete")

        except Exception as e:
            log.error("Failed to backup MySQL database")
            raise e

        finally:
            if output_file and not output_file.closed:
                output_file.close()

