# Deploy da aplicação no AWS

Foi realizado o deploy da aplicação no AWS. A api está disponível aqui <http://afe6a8d3a425b40739d688eb9c38c234-697055407.us-east-1.elb.amazonaws.com>

A aplicação foi hospedada em um cluster EKS (Elastic Kubernetes Service) e está disponível em um Load Balancer. A documentação foi gerada automaticamente pelo FastAPI e está disponível no endpoint `/docs`.

!!swagger openapi.json!!

## Realização do Deploy

Para realizar o deploy da aplicação no AWS, foi necessário seguir os seguintes passos (Após estar logado no AWS CLI):

1. Criar um cluster EKS:

```bash
eksctl create cluster --name fastapi-cluster --region us-east-1 --nodes 2
```

2. Configurar o kubectl para acessar o cluster:

```bash
aws eks --region us-east-1 update-kubeconfig --name fastapi-cluster
```

3. Criar um arquivo `db-deployment.yaml` com as configurações do deployment para a base de dados:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: postgres
spec:
  replicas: 1
  selector:
    matchLabels:
      app: postgres
  template:
    metadata:
      labels:
        app: postgres
    spec:
      containers:
      - name: postgres
        image: postgres:13
        env:
          - name: POSTGRES_USER
            value: "user"
          - name: POSTGRES_PASSWORD
            value: "password"
          - name: POSTGRES_DB
            value: "dbname"
        ports:
          - containerPort: 5432
---
apiVersion: v1
kind: Service
metadata:
  name: postgres
spec:
  ports:
    - port: 5432
  selector:
    app: postgres
```

4. Criar um arquivo `web-deployment.yaml` com as configurações do deployment para a aplicação:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fastapi
spec:
  replicas: 1
  selector:
    matchLabels:
      app: fastapi
  template:
    metadata:
      labels:
        app: fastapi
    spec:
      containers:
      - name: fastapi
        image: fernandoalzueta/apirest:web
        env:
          - name: DATABASE_URL
            value: "postgresql://user:password@postgres:5432/dbname"
        ports:
          - containerPort: 8000
---
apiVersion: v1
kind: Service
metadata:
  name: fastapi-service
spec:
  type: LoadBalancer
  ports:
    - port: 80
      targetPort: 8000
  selector:
    app: fastapi
```

5. Aplicar os deployments no cluster:

```bash
kubectl apply -f db-deployment.yml
kubectl apply -f web-deployment.yml
```

6. Acessar a aplicação no Load Balancer:

```bash
kubectl get svc fastapi-service
```
