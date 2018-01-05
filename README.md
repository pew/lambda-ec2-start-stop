# AWS EC2 Start/Stop Lambda

Use this lambda function together with cloudwatch events, and pass this to the function:

```
{
    "region": "us-east-1",
    "instance_id": "i-xxx",
}
```

if the instance is currently running, it'll stop the instance. if the instance is stopped, it'll start the instance.
