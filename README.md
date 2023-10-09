# App Clients

`Install`: You must have PIP to install this app. In your terminal locate the folder where you donwload the code. (Before install this I recommend to you actvate a venv)

`Install the application with`: 

```sh
pip install app_main
```

or if you want to edit the code and see changes in real time:

```sh
pip install --editable .
```

`Commands`: To ask for help 

```sh
app_main --help
```

`Create a client`: 

```sh
app_main clients create
``` 


`Delete a client`: 

```sh
app_main clients delete uid_client
``` 

`List all clients`: 

```sh
app_main clients read_list
``` 

`Update a client`: 

```sh
app_main clients update uid_client
```