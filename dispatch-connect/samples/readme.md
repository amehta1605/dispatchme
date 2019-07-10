The following libraries contain working code examples for both inbound and outbound processing using Dispatch Connect. It is recommended that you take these as a starting point as they should give you a big jump start.

# Inbound
The libraries contain both a `canonical` and `custom` payload example and you should pick the appropriate one depending on your use case:
- canonical - use this is if you intend on using Dispatch's canonical payload for sending data as defined in the [playbook](https://playbooks.dispatch.me)
- custom - use this is if you intend on sending through your own custom payload

These examples are fairly complete and can be used as is in your code. You of course will have to substitute the `payload` variable with data coming from your system. Also one other thing that's worth noting - the payload accepts an array (note the enclosing `[]`). So this means that you can send as many records in a single post as makes sense for your use case.

# Outbound
This contains the logic for polling the `agent/out` endpoint to retrieve any messages waiting to be picked up. The code logic will process and clear out all messages each time it runs. Poll the endpoint to pick up any updates as frequently as your business logic requires.
