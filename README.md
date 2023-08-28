### Run the server

```bash
cd src
pdm run uvicorn main:app --workers 8
```

### Call the POST method

```bash
curl -X POST "http://localhost:8000/items/" -H "accept: application/json" -H "Content-Type: application/json" -d '{"name":"item_post_route"}'
```


### Conclusion

We can see that if we open 2 terminals, and run:

```bash
pdm run tests/post.py test_111
```

then 1 ou 2 sec after:

```bash
pdm run tests/post.py test_222
```

We have this result (which means that the UoW are isolated in each thread)
```bash
--- START ---
Just register in UoW: name='item_post_route_test_111'
add 'item_post_route_test_111' to []
heavy work in progress...
--- START ---
Just register in UoW: name='item_post_route_test_222'
add 'item_post_route_test_222' to []
heavy work in progress...
Just register in UoW: name='another_inner_item'
add 'another_inner_item' to ['item_post_route_test_111']
Just register in UoW: name='inner_item'
add 'inner_item' to ['item_post_route_test_111', 'another_inner_item']
--- END ---
--- START ---
FROM UoW:
Model SAVED in DB: name='item_post_route_test_111'
FROM UoW:
Model SAVED in DB: name='another_inner_item'
FROM UoW:
Model SAVED in DB: name='inner_item'
INFO:     127.0.0.1:62013 - "POST /items/ HTTP/1.1" 200 OK
Just register in UoW: name='another_inner_item'
add 'another_inner_item' to ['item_post_route_test_222']
Just register in UoW: name='inner_item'
add 'inner_item' to ['item_post_route_test_222', 'another_inner_item']
--- END ---
--- START ---
FROM UoW:
Model SAVED in DB: name='item_post_route_test_222'
FROM UoW:
Model SAVED in DB: name='another_inner_item'
FROM UoW:
Model SAVED in DB: name='inner_item'
INFO:     127.0.0.1:62030 - "POST /items/ HTTP/1.1" 200 OK
```