from locust import HttpUser, between, task


class ModelPrediction(HttpUser):
    wait_time = between(1, 3)

    @task
    def predict_task(self):
        try:
            payload = {"feature1": 3.14,"feature2": 3.14}
            headers = {'Content-Type': 'application/json'}                        
            
            response = self.client.post("/predict", json=payload, headers=headers)
            
            if response.status_code == 200:

                self.environment.events.request_success.fire(
                    request_type="POST",
                    name="predict",
                    response_time=response.elapsed.total_seconds(),
                    response_length=len(response.text),
                )
            else:
                self.environment.events.request_failure.fire(
                    request_type="POST",
                    name="predict",
                    response_time=response.elapsed.total_seconds(),
                    exception=None,
                )
        except Exception as e:
            print(e)

# Exemplo de execução: locust -f nome-do-arquivo.py
