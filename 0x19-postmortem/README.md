# Postmortem

## My First Postmortem

### Issue Summary
**Duration:**  
- Start: 2024-06-10 14:00 UTC  
- End: 2024-06-10 15:30 UTC  

**Impact:**  
- Service Affected: Website and API services  
- User Experience: Users were unable to access the website, resulting in a 503 Service Unavailable error. API requests were also failing, affecting integrations and third-party services.  
- Affected Users: Approximately 75% of users were impacted, causing significant disruptions.

**Root Cause:**  
A configuration error in the load balancer caused it to improperly route traffic, resulting in server overload and service unavailability.

### Timeline
- **14:00 UTC**: Issue detected by automated monitoring systems reporting high error rates and slow response times.
- **14:05 UTC**: Engineer on-call received alert and began investigation.
- **14:10 UTC**: Initial assumption: High traffic volume causing server overload. Attempted to scale up servers.
- **14:20 UTC**: Scaling servers had no effect. Investigated server logs for errors.
- **14:30 UTC**: Noticed traffic not being evenly distributed. Suspected load balancer misconfiguration.
- **14:40 UTC**: Escalated to network team for further analysis of the load balancer.
- **14:50 UTC**: Network team confirmed misconfiguration in the load balancer.
- **15:00 UTC**: Network team reconfigured the load balancer to correct traffic routing.
- **15:15 UTC**: Services began to recover, and error rates decreased.
- **15:30 UTC**: Full service restoration confirmed.

### Root Cause and Resolution
**Root Cause:**  
The load balancer configuration was inadvertently changed during a routine update, causing it to route all traffic to a single server instead of distributing it evenly across multiple servers. This led to server overload and service failure.

**Resolution:**  
The network team identified the incorrect configuration and reverted it to the previous stable state. Traffic was then correctly distributed across the servers, allowing them to handle the load efficiently and restoring normal service.

### Corrective and Preventative Measures
**Improvements/Fixes:**  
1. Implement stricter change management protocols to review and verify configuration changes before deployment.
2. Enhance monitoring to detect load balancer configuration issues more quickly.
3. Conduct regular training for the network and operations teams on best practices for load balancer management.

**Tasks to Address the Issue:**  
- [ ] Patch the load balancer with updated configuration validation checks.
- [ ] Add detailed monitoring and alerting for load balancer configurations.
- [ ] Update documentation on load balancer configurations and include a rollback procedure.
- [ ] Schedule a review meeting to discuss the incident and preventive measures.
- [ ] Implement automated tests to verify load balancer configurations before deployment.

### Conclusion
This postmortem has outlined the incident affecting our web and API services due to a load balancer misconfiguration. By implementing the corrective and preventive measures listed, we aim to prevent such incidents in the future and ensure higher reliability and availability of our services.
