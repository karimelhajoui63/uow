### Run the server

```bash
uvicorn main:app --reload
```

### Call the POST method

```bash
curl -X POST "http://localhost:8000/items/" -H "accept: application/json" -H "Content-Type: application/json" -d '{"name":"item_post_route"}'
```