doc



docker build -t case .
docker run --name case19 -p 8000:8000 case
http://127.0.0.1:8000/docs