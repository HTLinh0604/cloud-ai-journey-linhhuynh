---
title: "Week 6"
date: 2026-05-25
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---

**Weekly objectives:**
- Understand DynamoDB Streams and configure Lambda triggers for event-driven databases.
- Analyze DynamoDB Global Tables configuration for multi-region active-active replication.
- Configure DynamoDB Accelerator (DAX) caching to reduce read latency.
- Manage RDS Multi-AZ configurations and evaluate database scalability.

**Tasks to be deployed this week:**

| Day | Task | Date |
|---|---|---|
| Monday | Studied DynamoDB Streams record types (INSERT, MODIFY, REMOVE). Configured a stream trigger to invoke a Lambda function for item change auditing. | May 25 |
| Tuesday | Explored DynamoDB Global Tables replication behavior. Configured multi-region active-active replication, analyzing sync latency and conflict resolution policies. | May 26 |
| Wednesday | Provisioned a DynamoDB Accelerator (DAX) cluster. Configured application clients to route read requests through the DAX cache to evaluate performance. | May 27 |
| Thursday | Analyzed RDS Multi-AZ failover and Read Replica configurations. Evaluated replication lag and read throughput scalability across replicas. | May 28 |
| Friday | Compared NoSQL and SQL databases. Evaluated schemas, query capabilities, scalability, and transaction support to choose the correct model. | May 29 |

**Weekly results achieved:**
- **Monday:**
  - Result Achieved: Active DynamoDB stream with Lambda trigger logging database changes to CloudWatch.
  - Lesson: DynamoDB Streams enables reactive, event-driven databases by capturing and processing item modifications.
- **Tuesday:**
  - Result Achieved: Verified active-active write capability across multiple regions using global tables.
  - Lesson: Global tables provide multi-region disaster recovery and low-latency local access for distributed users.
- **Wednesday:**
  - Result Achieved: Verified cache hit rates and measured read query response latency decrease.
  - Lesson: DAX reduces query latency from milliseconds to microseconds, offloading database read capacity requirements.
- **Thursday:**
  - Result Achieved: Verified simulated failovers and scaled read operations using database read replicas.
  - Lesson: Multi-AZ deployments provide high availability, while read replicas resolve database read bottlenecks.
- **Friday:**
  - Result Achieved: Completed a database selection matrix document mapping workloads to DynamoDB or RDS PostgreSQL.
  - Lesson: SQL databases are best for complex relationship queries; NoSQL is suited for massive horizontal scale.

