# 🚀 DevOps Monitoring & Alerting Homelab

> **"Monitoring tells you what's happening. Observability tells you why."**

<p align="center">

<img src="https://img.shields.io/badge/Prometheus-Monitoring-orange?style=for-the-badge&logo=prometheus">
<img src="https://img.shields.io/badge/Grafana-Dashboard-F46800?style=for-the-badge&logo=grafana">
<img src="https://img.shields.io/badge/Alertmanager-Alerting-red?style=for-the-badge">
<img src="https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge&logo=postgresql">
<img src="https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker">

</p>

---

# 🌍 Welcome to the Monitoring Control Room

Imagine you're responsible for a production application.

Everything is running smoothly until suddenly users begin reporting problems.

- The website becomes slow.
- API requests start failing.
- Database connections keep increasing.
- CPU usage spikes.
- Disk space begins running out.

Now imagine trying to figure out the problem by logging into multiple servers, checking logs one by one, and guessing where the issue started.

That approach doesn't scale.

This project demonstrates how modern DevOps teams solve that challenge using **Prometheus**, **Grafana**, **Alertmanager**, **Node Exporter**, and **PostgreSQL Exporter**.

Instead of reacting after users complain, the monitoring system continuously watches every layer of the application, detects problems early, groups related alerts to reduce noise, and immediately notifies the right team with actionable information.

---

# 🎯 Project Goal

The goal of this project is to build a production-inspired monitoring and alerting platform for a multi-tier application.

Rather than monitoring only servers, this project provides visibility across the complete application stack, allowing engineers to quickly determine whether an issue originates from the frontend, backend API, PostgreSQL database, or the underlying infrastructure.

By combining infrastructure monitoring, database monitoring, intelligent alerting, and centralized dashboards, this project demonstrates how observability can significantly reduce troubleshooting time.

---

# 🏗 Project Architecture

```text
                                      🌍 Users
                                         │
                                         ▼

                               ┌─────────────────┐
                               │ Web Frontend    │
                               └─────────────────┘
                                         │
                                         ▼

                               ┌─────────────────┐
                               │ Backend API     │
                               └─────────────────┘
                                         │
                                         ▼

                               ┌─────────────────┐
                               │ PostgreSQL      │
                               └─────────────────┘


                ┌──────────────────────────────┐
                │                              │
                ▼                              ▼

       ┌──────────────────┐          ┌─────────────────────┐
       │ Node Exporter    │          │ PostgreSQL Exporter │
       └──────────────────┘          └─────────────────────┘

                │                              │
                └──────────────┬───────────────┘
                               │
                               ▼

                      ┌────────────────────┐
                      │    Prometheus      │
                      │ Metric Collection  │
                      └────────────────────┘
                               │

                     Evaluate Alert Rules
                               │
                               ▼

                     ┌────────────────────┐
                     │   Alertmanager     │
                     └────────────────────┘
                               │

        Group Alerts • Route Alerts • Reduce Alert Fatigue

                               │
                               ▼

                        Slack Notifications

                               │
                               ▼

                        👨‍💻 DevOps Engineer
```

---

# 🚀 Technologies Used

This project is built using Docker Compose to orchestrate multiple services into a single monitoring environment.

Prometheus acts as the monitoring engine by scraping metrics from every exporter, while Grafana transforms those metrics into easy-to-understand dashboards.

Alertmanager is responsible for grouping alerts, reducing alert fatigue, and routing notifications based on severity.

Node Exporter continuously collects operating system metrics, and PostgreSQL Exporter exposes database metrics that help monitor database health and performance.

Together, these tools create a complete observability platform similar to what many DevOps and SRE teams use in production.

---

# 🔍 What This Project Monitors

Instead of monitoring only one component, the monitoring stack observes every important layer of the application.

```text
Users

↓

Frontend

↓

Backend API

↓

Database

↓

Operating System

↓

Infrastructure
```

This layered approach makes it easy to identify exactly where a problem starts.

For example, if the frontend becomes unavailable while the backend and database remain healthy, engineers immediately know the issue is isolated to the web layer instead of wasting time investigating the database.

---

# 📊 Infrastructure Monitoring

Infrastructure metrics are collected using **Node Exporter**.

The monitoring platform continuously tracks CPU utilization, memory usage, disk consumption, filesystem health, network traffic, system load, and many other operating system metrics.

These metrics provide early warning signs before resource exhaustion begins affecting application performance.

---

# 🗄 Database Monitoring

Database metrics are collected using **postgres_exporter**.

The monitoring platform continuously watches active connections, connection utilization, database availability, query activity, and overall database health.

Monitoring these metrics helps identify issues such as connection exhaustion long before the database reaches its maximum capacity.

---

# 🚨 Intelligent Alerting

One of the biggest challenges in monitoring is alert fatigue.

Receiving dozens of notifications for the same incident quickly becomes overwhelming and makes it difficult to identify the real problem.

To solve this, Alertmanager intelligently groups alerts by service and severity before sending notifications.

Instead of receiving multiple Slack messages for CPU, memory, and disk issues individually, engineers receive a single grouped notification that summarizes everything happening within the affected service.

This makes alerts much easier to understand and significantly reduces notification noise.

---

# ⚠ Severity-Based Alerting

Not every issue should wake someone up in the middle of the night.

For that reason, alerts are categorized into different severity levels.

Warning alerts notify engineers about issues that should be investigated before they become critical.

Critical alerts indicate that immediate action is required because the application or infrastructure is at risk.

This approach allows teams to prioritize incidents based on business impact instead of treating every alert the same way.

---

# 🔀 Alert Routing

Once an alert is generated by Prometheus, it is sent to Alertmanager.

Alertmanager evaluates the alert, groups similar alerts together, determines its severity, and routes it to the appropriate notification channel.

This ensures the correct team receives the correct alert without unnecessary duplication.

```text
Prometheus

      │

      ▼

Alertmanager

      │

      ├──────────────┐

      ▼              ▼

 Warning         Critical

      │              │

      ▼              ▼

 Slack A        Slack B
```

---

# 📈 Monitoring Workflow

```text
Application Running

        │

        ▼

Exporters Collect Metrics

        │

        ▼

Prometheus Scrapes Metrics

        │

        ▼

Prometheus Evaluates Rules

        │

Threshold Crossed?

   │            │

  No           Yes

   │            │

   ▼            ▼

 Continue   Generate Alert

                  │

                  ▼

           Alertmanager

                  │

       Group Similar Alerts

                  │

                  ▼

       Route Based On Severity

                  │

                  ▼

        Slack Notification

                  │

                  ▼

          DevOps Engineer
```

---

# 📁 Project Structure

```
DevOps-Monitoring-Homelab/

│

├── docker-compose.yml

│

├── prometheus/

│     ├── prometheus.yml

│     ├── alert.rules.yml

│

├── alertmanager/

│     └── alertmanager.yml

│

├── grafana/

│     ├── provisioning/

│     ├── dashboards/

│

├── postgres/

│

├── exporters/

│     ├── node_exporter/

│     └── postgres_exporter/

│

└── README.md
```

---

# 🌟 Why I Built This Project

I wanted to move beyond simply running monitoring tools and instead build a complete observability platform that resembles what DevOps teams use in production.

This project gave me hands-on experience with monitoring multiple application layers, collecting infrastructure and database metrics, writing Prometheus alert rules, configuring Alertmanager for intelligent routing, reducing alert fatigue through grouping, and visualizing system health using Grafana dashboards.

More importantly, it helped me understand that monitoring is not just about collecting metrics—it's about helping engineers quickly identify, understand, and resolve problems before users are affected.

---

# ⚙️ Getting Started

Setting up the monitoring stack is straightforward thanks to Docker Compose. Every service runs inside its own container, making the environment portable and easy to reproduce on any machine.

---

# 📦 Prerequisites

Before running the project, make sure the following software is installed on your system:

- Docker
- Docker Compose
- Git

Verify the installation using:

```bash
docker --version
docker compose version
git --version
```

---

# 📥 Clone the Repository

Clone the repository to your local machine.

```bash
git clone https://github.com/<your-username>/DevOps-Monitoring-Homelab.git

cd DevOps-Monitoring-Homelab
```

---

# 🚀 Start the Monitoring Stack

Launch every service using Docker Compose.

```bash
docker compose up -d
```

Docker will automatically create the required network, pull all container images, and start every service.

To verify that everything is running correctly:

```bash
docker ps
```

You should see containers similar to:

```
✔ Prometheus

✔ Grafana

✔ Alertmanager

✔ PostgreSQL

✔ Node Exporter

✔ PostgreSQL Exporter

✔ Backend API

✔ Frontend
```

---

# 🌐 Access the Services

Once all containers are running, open the following services in your browser.

| Service | URL |
|----------|-----|
| Frontend | http://localhost |
| Backend API | http://localhost:3000 |
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:3001 |
| Alertmanager | http://localhost:9093 |
| PostgreSQL Exporter | http://localhost:9187/metrics |
| Node Exporter | http://localhost:9100/metrics |

---

# 🔄 Complete Monitoring Flow

The monitoring pipeline follows a simple but powerful workflow.

```text
Application

      │

      ▼

Frontend

      │

      ▼

Backend API

      │

      ▼

PostgreSQL

      │

      ▼

Exporters expose metrics

      │

      ▼

Prometheus scrapes metrics

      │

      ▼

Prometheus evaluates rules

      │

      ▼

Alertmanager groups alerts

      │

      ▼

Slack Notification

      │

      ▼

Engineer investigates

      │

      ▼

Grafana Dashboard
```

---

# 📡 Prometheus Configuration

Prometheus acts as the heart of the monitoring platform.

Every few seconds it visits each exporter, collects fresh metrics, stores them in its time-series database, and evaluates alert rules.

Instead of applications pushing metrics, Prometheus follows a pull model where it continuously scrapes every configured target.

Example configuration:

```yaml
scrape_configs:

- job_name: node-exporter

  static_configs:

  - targets:

      - node_exporter:9100

- job_name: postgres-exporter

  static_configs:

  - targets:

      - postgres_exporter:9187

- job_name: backend-api

  static_configs:

  - targets:

      - backend:3000
```

Each scrape job tells Prometheus exactly where metrics are exposed.

---

# 🖥 Node Exporter

Node Exporter provides visibility into the operating system.

Instead of monitoring Docker containers only, it exposes metrics directly from the host machine.

Some of the metrics collected include:

- CPU utilization
- Memory usage
- Filesystem usage
- Disk IO
- Network traffic
- System load
- Uptime
- Running processes

These metrics help identify infrastructure bottlenecks before they affect applications.

---

# 🗄 PostgreSQL Exporter

The PostgreSQL exporter continuously collects database metrics.

This includes:

- Active connections
- Maximum connection usage
- Database availability
- Query statistics
- Transaction activity
- Database health

These metrics allow engineers to identify issues such as connection exhaustion, unhealthy databases, or performance degradation.

---

# 📊 Grafana Dashboards

Raw metrics are difficult to understand.

Grafana transforms those numbers into visual dashboards that make it easy to understand the health of the system at a glance.

The dashboards display information such as:

- CPU usage
- Memory utilization
- Disk consumption
- Network traffic
- Database connections
- Database health
- System availability
- Alert status

Instead of reading thousands of metrics, engineers can quickly identify trends and anomalies through interactive charts.

---

# 🚨 Alert Engineering

Monitoring becomes truly valuable when it can notify engineers before users are impacted.

This project includes multiple alert rules covering infrastructure and database health.

Examples include:

```
High CPU Usage

↓

Warning
```

```
Memory Usage High

↓

Warning
```

```
Disk Almost Full

↓

Critical
```

```
Database Connections High

↓

Critical
```

```
PostgreSQL Down

↓

Critical
```

Each alert includes:

- Alert Name
- Severity
- Description
- Instance
- Service

This makes every notification meaningful and actionable.

---

# 🎯 Alert Severity

Instead of treating every alert the same, alerts are divided into two categories.

### 🟡 Warning

A warning alert indicates that something is starting to become unhealthy.

Examples include:

- CPU above 70%
- Database connections above 60%
- Memory usage increasing

These alerts provide enough time to investigate before users notice any issues.

---

### 🔴 Critical

Critical alerts indicate immediate action is required.

Examples include:

- PostgreSQL unavailable
- Disk almost full
- CPU above 95%
- Database connections above 85%

Critical alerts are routed with higher priority because they may impact application availability.

---

# 🧠 Smart Alert Grouping

One incident can generate many alerts.

For example:

```
Backend CPU High

Backend Memory High

Backend Disk High

Backend Network High
```

Without grouping, engineers receive four separate notifications.

Instead, Alertmanager groups related alerts by **service** and **severity**.

```
Backend

Severity : Critical

Affected Resources

• CPU

• Memory

• Disk

• Network
```

This dramatically reduces alert fatigue while keeping important information together.

---

# 📬 Alert Routing

After Prometheus generates an alert, Alertmanager decides where that alert should go.

Routing is based on labels such as:

- Service
- Severity
- Team

Example workflow:

```text
Alert Generated

        │

        ▼

Alertmanager

        │

        ├──────────────┐

        ▼              ▼

 Warning         Critical

        │              │

        ▼              ▼

Slack Team A    Slack Team B
```

This ensures every alert reaches the correct team without overwhelming everyone.

---

# 📈 Example PromQL Queries

Prometheus uses PromQL to query metrics.

Some useful examples include:

Current CPU usage

```promql
100 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100
```

Memory usage

```promql
(node_memory_MemTotal_bytes-node_memory_MemAvailable_bytes)
/
node_memory_MemTotal_bytes
*100
```

Database connections

```promql
pg_stat_activity_count
```

Database connection utilization

```promql
instance:pg_connections:ratio
```

These queries power both dashboards and alert rules.

---

# 📷 Screenshots

You can add screenshots here to showcase the project.

```
screenshots/

├── grafana-dashboard.png

├── prometheus-targets.png

├── alertmanager-ui.png

├── slack-alert.png

└── postgres-dashboard.png
```

Example:

## Grafana Dashboard

> *(Add Screenshot Here)*

---

## Prometheus Targets

> *(Add Screenshot Here)*

---

## Alertmanager

> *(Add Screenshot Here)*

---

## Slack Notification

> *(Add Screenshot Here)*

---

# 💡 Why This Matters

A monitoring platform is much more than a collection of dashboards.

It acts as an early warning system for the entire application.

Instead of waiting for customers to report problems, engineers are notified immediately with enough context to understand where the issue originated, how severe it is, and what needs attention first.

That is the ultimate goal of observability—not just collecting metrics, but helping teams detect, understand, and resolve incidents faster.
---
# 🎯 Real-World Scenarios

This project was designed to simulate situations that DevOps engineers commonly face in production environments.

Imagine a database suddenly starts running out of available connections. Instead of waiting for users to report failures, Prometheus detects the increasing connection utilization, Alertmanager groups related alerts, and a notification is immediately sent to the appropriate Slack channel. Engineers can quickly open Grafana, inspect the database dashboard, identify the root cause, and resolve the issue before it impacts customers.

The same workflow applies to infrastructure problems such as high CPU utilization, memory exhaustion, disk space issues, or application failures.

---

# 💡 Lessons Learned

Building this project taught me much more than simply installing monitoring tools.

I learned how metrics flow from exporters to Prometheus, how Prometheus evaluates alert rules, how Alertmanager intelligently groups and routes alerts, and how Grafana transforms raw metrics into meaningful dashboards.

More importantly, I learned that good monitoring is not about collecting thousands of metrics—it is about collecting the right metrics and presenting them in a way that helps engineers quickly understand and resolve problems.

I also gained practical experience in designing alert thresholds, reducing alert fatigue, and organizing monitoring around services rather than individual machines.

---

# 🚀 Challenges Faced

Like any real-world project, this one came with its own challenges.

One of the biggest challenges was avoiding alert fatigue. Initially, every metric crossing a threshold generated separate notifications, making it difficult to focus on the actual problem.

To solve this, I configured Alertmanager to group alerts based on **service** and **severity**, ensuring that related alerts were combined into a single notification.

Another challenge was selecting meaningful thresholds. Rather than triggering alerts for every small spike, I used warning and critical severity levels along with the `for` duration in Prometheus alert rules. This helped filter out temporary spikes and reduced false positives.

I also learned how exporters expose metrics differently and how PromQL can be used to build more meaningful alert conditions instead of relying on fixed values.

---

# 📚 Skills Demonstrated

Through this project, I gained practical experience with several DevOps concepts including monitoring, observability, alert engineering, infrastructure monitoring, database monitoring, PromQL, Docker networking, service discovery, and dashboard visualization.

I also strengthened my understanding of production troubleshooting by learning how different layers of an application interact and how monitoring can quickly identify the failing component.

---

# 🌟 Why This Project Stands Out

Many monitoring projects demonstrate only a single tool or monitor a single server.

This project takes a broader approach by monitoring a complete multi-tier application consisting of a web frontend, backend API, PostgreSQL database, operating system metrics, and infrastructure health.

It also goes beyond simple metric collection by implementing intelligent alerting, alert grouping, severity-based routing, and production-inspired monitoring practices.

The focus is not only on collecting data but on making that data useful for troubleshooting and incident response.

---

# 🔮 Future Improvements

Although the current monitoring platform provides a strong foundation, there are many opportunities to expand it further.

Future enhancements include integrating Kubernetes monitoring, Helm charts, cAdvisor for container metrics, Blackbox Exporter for endpoint monitoring, Loki and Promtail for centralized logging, Tempo or Jaeger for distributed tracing, Terraform for infrastructure provisioning, GitHub Actions or Jenkins for CI/CD automation, and PagerDuty for advanced incident management.

These additions would transform the project into a complete observability platform covering metrics, logs, traces, infrastructure, and deployment automation.

---

# 💼 Interview Talking Points

This project gave me hands-on experience with several production-inspired DevOps practices.

During interviews, I can confidently discuss topics such as:

- Designing monitoring for multi-tier applications.
- Choosing meaningful metrics for infrastructure and databases.
- Writing PromQL queries for dashboards and alerts.
- Creating warning and critical alert thresholds.
- Reducing alert fatigue through intelligent alert grouping.
- Configuring Alertmanager routing based on severity.
- Monitoring PostgreSQL using postgres_exporter.
- Monitoring Linux systems using Node Exporter.
- Visualizing system health using Grafana.
- Troubleshooting incidents using dashboards and alerts.

Rather than discussing these concepts only from theory, I can explain how they were implemented in this project and the reasoning behind each design decision.

---

---

# 📸 Project in Action

One of the best ways to understand a monitoring platform is to see it in action. The screenshots below demonstrate how Prometheus, Grafana, and Alertmanager work together to provide complete visibility into the application while reducing alert fatigue.

---

# 📊 Grafana Dashboard

Grafana acts as the visualization layer of the monitoring stack. Instead of manually checking each service, engineers can quickly understand the health of the entire application from a single dashboard.

<p align="center">
  <img src="./screenshots/grafana-dashboard.png" alt="Grafana Dashboard" width="95%">
</p>

The dashboard is organized into three logical services:

- 🌐 Web Service
- ⚙️ API Service
- 🗄️ Database Service

Each service contains dedicated panels displaying health, availability, request metrics, application errors, and database performance. Grouping dashboards by service makes troubleshooting much faster because the failing layer can be identified within seconds.

---

# 🚨 Prometheus Alert Rules

Prometheus continuously evaluates custom PromQL alert rules to determine whether the application is healthy.

<p align="center">
  <img src="./screenshots/alert-rule.png" alt="Alert Rule" width="85%">
</p>

This project uses multiple alert rules with different thresholds.

For example:

- Warning alerts notify engineers when a metric begins to trend in the wrong direction.
- Critical alerts indicate that immediate action is required.

Each alert contains useful metadata such as:

- Alert Name
- Service
- Severity
- Description
- Instance

This makes notifications meaningful instead of simply saying "Something is wrong."

---

# 🔥 Active Prometheus Alerts

Whenever an alert condition remains true for the configured duration, Prometheus marks the alert as **Firing**.

<p align="center">
  <img src="./screenshots/active-alerts.png" alt="Prometheus Alerts" width="85%">
</p>

The screenshot above shows both **Warning** and **Critical** alerts being triggered simultaneously.

This allows engineers to immediately distinguish between issues that require investigation and incidents that require urgent action.

---

# 🧠 Alert Grouping

One of the primary goals of this project is reducing **alert fatigue**.

Without grouping, a single incident could generate dozens of notifications.

For example:

```
CPU High

Memory High

Disk High

Filesystem High

Network High
```

Instead of receiving five different Slack messages, Alertmanager groups alerts together using labels such as:

- Service
- Severity
- Alert Name

Result:

```
Backend Service

Severity : Critical

Affected Resources

• CPU

• Memory

• Disk
```

This dramatically reduces notification noise and makes incidents much easier to understand.

---

# 💬 Slack Notifications

Once Alertmanager receives alerts from Prometheus, it automatically routes notifications to Slack.

<p align="center">
  <img src="./screenshots/slack-alerts.png" alt="Slack Notification" width="60%">
</p>

Each notification contains:

- Alert Name
- Severity
- Service
- Instance
- Description

Instead of generic notifications, engineers receive enough information to immediately begin troubleshooting.

---

# 🔄 End-to-End Monitoring Flow

```text
                   User Request
                         │
                         ▼
                 Web Frontend
                         │
                         ▼
                   Backend API
                         │
                         ▼
                    PostgreSQL
                         │
     ┌───────────────────┴────────────────────┐
     │                                        │
     ▼                                        ▼
Node Exporter                        PostgreSQL Exporter
     │                                        │
     └───────────────────┬────────────────────┘
                         ▼
                    Prometheus
              Scrape → Store → Evaluate
                         │
                  Alert Rules Trigger
                         │
                         ▼
                   Alertmanager
                         │
         Group Alerts • Route Alerts
                         │
                         ▼
               Slack Notifications
                         │
                         ▼
                 👨‍💻 DevOps Engineer
```

---

# 📂 Screenshots Folder Structure

```
screenshots/
│
├── grafana-dashboard.png
├── alert-rule.png
├── active-alerts.png
├── slack-alerts.png
└── alertmanager-grouping.png
```

Simply place your screenshots inside the `screenshots` directory using the filenames above. GitHub will automatically render them in the README.

---

# 🎬 Demo

The following workflow demonstrates how the monitoring platform behaves during an incident:

1. A user request reaches the application.
2. Exporters expose infrastructure and database metrics.
3. Prometheus scrapes metrics at regular intervals.
4. Alert rules are evaluated using PromQL.
5. When a threshold is exceeded, Prometheus generates an alert.
6. Alertmanager groups related alerts by service and severity.
7. Slack receives a clean, actionable notification.
8. Engineers use Grafana dashboards to investigate and resolve the issue.
