session.execute(
    """
    INSERT INTO users (familyName, firstName, age, address, phone, uuid)
    VALUES (%(familyName)s, %(firstName)s, %(age)s, %(address)s, %(phone)s, %(uuid)s,)
    """,
    {'familyName': "j1", 'firstName': j2, 'age': 40, 'address' : "paris", 'phone' : "+33687453287", 'uuid' : uuid.uuid1()}
)     


query = "SELECT * FROM users WHERE user_id=%s"
future = session.execute_async(query, [user_id])

# ... do some other work

try:
    rows = future.result()
    user = rows[0]
    print user.name, user.age
except ReadTimeout:
    log.exception("Query timed out:")


# build a list of futures
futures = []
query = "SELECT * FROM users WHERE user_id=%s"
for user_id in ids_to_fetch:
    futures.append(session.execute_async(query, [user_id])

# wait for them to complete and use the results
for future in futures:
    rows = future.result()
    print rows[0].name


def handle_success(rows):
    user = rows[0]
    try:
        process_user(user.name, user.age, user.id)
    except Exception:
        log.error("Failed to process user %s", user.id)
        # don't re-raise errors in the callback

def handle_error(exception):
    log.error("Failed to fetch user info: %s", exception)


future = session.execute_async(query)
future.add_callbacks(handle_success, handle_error)