---
title: "Sharing and Feedback"
date: 2024-01-01
weight: 7
chapter: false
pre: " <b> 7. </b> "
---

# Sharing and Feedback

> *This section shares my personal reflections and honest feedback about the **First Cloud AI Journey (FCAJ)** program. I hope these thoughts are useful to the FCJ team and future participants.*

---

## 1. Overall Impression of the Program

Joining FCAJ was one of the most practically valuable experiences I have had as a cloud learner. Unlike typical online courses where you follow pre-configured demos, FCAJ pushed me to build something real from scratch - designing the architecture, writing the code, debugging real errors, and documenting every step.

The program's structure was well thought out: it gave enough guidance to prevent participants from getting completely lost, but left enough room for us to make our own decisions and learn from the consequences. That balance - structured yet open-ended - is what made the experience genuinely educational rather than just a guided tutorial.

As team leader, I also gained skills beyond the technical: I learned how to coordinate people with different experience levels, how to communicate priorities under time pressure, and how to keep the team motivated when things were not working as expected.

---

## 2. Satisfaction Level

**Overall satisfaction: ⭐⭐⭐⭐ (4/5)**

| Aspect | Satisfaction | Notes |
|--------|-------------|-------|
| Technical depth of content | ⭐⭐⭐⭐⭐ | Excellent - real AWS services, real architecture, real debugging |
| Program structure & guidance | ⭐⭐⭐⭐⭐ | Clear and well-paced; some steps could use more example screenshots |
| Support from mentors/admin | ⭐⭐⭐⭐⭐ | Responsive and helpful; I appreciated the open Q&A culture |
| Relevance to real-world work | ⭐⭐⭐⭐⭐ | Very high - the Medallion Lakehouse pattern is industry-standard |
| Time allocation | ⭐⭐⭐ | Some sections felt rushed; more time for the ETL and monitoring steps would help |

---

## 3. Areas for Improvement

While my overall experience was very positive, I have a few constructive suggestions for the FCJ team:

**a) More context on FinOps from the start**
The cost optimization aspect of the architecture (Parquet, Athena workgroups, Glue DPU sizing) was interesting but introduced late. If participants understood the cost rationale from the beginning, it would help them make better design decisions throughout.

**b) A pre-built "starter" environment option**
Setting up the VPC, IAM roles, and S3 bucket from scratch takes considerable time at the beginning. Offering an optional CloudFormation/Terraform template for participants who want to focus purely on the data engineering aspects would be helpful - without making it mandatory, to preserve the learning value.

**c) More structured troubleshooting guidance**
When a Glue job fails or an Athena query returns no results, first-time participants can feel overwhelmed. A dedicated "Common Issues & How to Debug" reference page within the workshop documentation would significantly reduce frustration.

**d) Peer review session**
Adding a short session where teams present their architecture to each other and receive feedback would create a great learning experience and encourage different approaches to the same problem.

---

## 4. Would I Recommend This Program to Friends?

**Yes, absolutely - and I already have.**

I would recommend FCAJ to:

- **Students and early-career developers** who have learned AWS theory but have never built a complete, production-like architecture on their own
- **Anyone interested in Data Engineering** - the Glue + Athena + S3 stack is directly applicable to real data platform roles
- **Team-oriented learners** - the collaborative format makes the experience much richer than studying alone

**Why?** Because FCAJ closes the gap between "I know what S3 is" and "I can design and implement a data lakehouse on AWS." That gap is exactly where most self-learners get stuck. The program provides the structure, the real AWS environment, and the community to push through it.

The hands-on format means you finish the program with something tangible: a working pipeline, documented code, and the confidence to explain every architectural decision you made. That is far more valuable than a certificate from a course you watched on 1.5x speed.

---

## 5. Closing Message

Thank you to the **FCJ team** for creating and running this program. The effort that went into designing the workshop content, supporting participants, and building a community around cloud learning is evident.

For future participants: **do not be afraid to make mistakes.** Some of the most valuable learning moments in this workshop came from debugging broken Glue jobs at midnight or figuring out why the Streamlit dashboard was refusing connections. Those moments of friction are where real understanding is built.

> *"The best way to learn cloud architecture is to break something and fix it."* - A lesson FCAJ taught me well.
