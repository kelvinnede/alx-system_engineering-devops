# Web Stack Debugging 4

## Task 0: Sky is the limit, let's bring that limit higher

In this task, we are testing the performance of our Nginx web server under load using ApacheBench. The initial test results showed a high number of failed requests, indicating that the server was not handling the load effectively.

### Issue Summary

- **Duration:** The issue was identified during benchmarking.
- **Impact:** Affected 943 out of 2000 requests, resulting in a failure rate of 47.15%. Users experienced failed requests and non-2xx responses.
- **Root Cause:** Insufficient worker connections and processes configured in Nginx.

### Timeline

- **Issue Detected:** During ApacheBench benchmarking.
- **How Detected:** Benchmarking test.
- **Actions Taken:**
  - Reviewed Nginx configuration.
  - Identified limits on worker connections and processes.
- **Resolution:** Increased the number of worker connections and processes.
- **Incident Escalated to:** N/A
- **Final Resolution:** Applied the fix using Puppet and confirmed with ApacheBench.

### Root Cause and Resolution

- **Root Cause:** The default configuration of Nginx was not optimized to handle a high number of concurrent connections, leading to many failed requests.
- **Resolution:** Modified Nginx configuration to increase worker connections to 1024 and set worker processes to auto.

### Corrective and Preventative Measures

- **Improvements:**
  - Optimize Nginx configurations for high traffic.
  - Monitor server performance continuously.
- **Tasks:**
  - Update Nginx configuration.
  - Implement monitoring tools for performance metrics.

## Usage

To apply the fix, run the following command:

```sh
puppet apply 0-the_sky_is_the_limit_not.pp
