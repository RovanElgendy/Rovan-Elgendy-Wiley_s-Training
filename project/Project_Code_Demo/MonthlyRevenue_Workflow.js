{
    "job_id": 1124607496355303,
    "creator_user_name": "rovanelgendy@outlook.com",
    "run_as_user_name": "rovanelgendy@outlook.com",
    "run_as_owner": true,
    "settings": {
        "name": "MonthlyRevenue",
        "email_notifications": {
            "on_start": [
                "rovanelgendy@outlook.com"
            ],
            "on_success": [
                "rovanelgendy@outlook.com"
            ],
            "on_failure": [
                "rovanelgendy@outlook.com"
            ],
            "no_alert_for_skipped_runs": false
        },
        "webhook_notifications": {},
        "timeout_seconds": 0,
        "schedule": {
            "quartz_cron_expression": "11 0 23 31 * ?",
            "timezone_id": "UTC",
            "pause_status": "UNPAUSED"
        },
        "max_concurrent_runs": 1,
        "tasks": [
            {
                "task_key": "MonthlyRevenue",
                "notebook_task": {
                    "notebook_path": "project/Project_Code_Demo/Azure Databricks Project notebook",
                    "source": "GIT"
                },
                "existing_cluster_id": "0404-085334-6dpr0fdv",
                "timeout_seconds": 0,
                "email_notifications": {}
            }
        ],
        "git_source": {
            "git_url": "https://github.com/RovanElgendy/Rovan-Elgendy-Wiley_s-Training",
            "git_provider": "gitHub",
            "git_branch": "main"
        },
        "format": "MULTI_TASK"
    },
    "created_time": 1680645130579
}
