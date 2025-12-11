from locust import HttpUser, task, between

class ReqresUser(HttpUser):
    # Wait time between tasks to simulate real user behavior
    wait_time = between(1, 3)

    @task
    def list_users(self):
        """
        Simple load test hitting:
        GET https://reqres.in/api/users?page=2
        """
        self.client.get("/api/users?page=2")
