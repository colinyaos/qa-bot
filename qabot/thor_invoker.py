# bash_job_invoker.py

import json
import os
import logging
from lib.thorlib import send_get_request, send_post_request, send_put_request, ThorLib

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
log = logging.getLogger(__name__)


class thor_invoker:
    # Hermod
    def start_release(release_name):
        """
        Starts a release in thor.
        Eventual invoke syntax:
        @qa-bot start-release <release_name>
        """
        thorlib = ThorLib()
        response = thorlib.send_post_request(f"/releases/{release_name}/start")

        if response["status_code"] == 200:
            return "Started release {}".format(release_name)
        else:
            return "Failed to start release {}".format(release_name)

    def restart_release(release_name):
        """
        Restarts a release in thor.
        Eventual invoke syntax:
        @qa-bot restart-release <release_name>
        """
        thorlib = ThorLib()
        response = thorlib.send_post_request(f"/releases/{release_name}/restart")

        if response["status_code"] == 200:
            return "Restarted release {}".format(release_name)
        else:
            return "Failed to restart release {}".format(release_name)

    def check_release_status():
        # not implemented yet
        return

    def get_task_failure_data():
        # not implemented yet, plus waiting on implementation in main
        return

    def schedule_release():
        # not implemented yet, unsure if this is desired
        return
