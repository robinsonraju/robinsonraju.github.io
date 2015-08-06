---
layout: post
title:  "What is agile and what are user stories"
date:   2014-09-09 22:54:56
categories: Agile 
---
<img src="/images/agile-development.jpg" width="320"/>

# Introduction

In the earlier days of the software industry, the process of developing software products mirrored engineering practices of the day. Like a bridge construction needed elaborate planning, design and construction, a software product went through a “waterfall” model of requirement definition, design, development, testing and release, with each phase occurring one after another.

But the cookie cutter approach failed for big software products which ended up creating products and systems that user didn’t have in mind or didn’t want anymore or became obsolete because the technology had changed. This is where Agile methodology comes into light.

# What is Agile? 

> Agile software development is a group of software development methods in which requirements and solutions evolve through collaboration between self-organizing, cross-functional teams. It promotes adaptive planning, evolutionary development, early delivery, continuous improvement and encourages rapid and flexible response to change. It is a conceptual framework that focuses on frequently delivering small increments of working software. 

# Short History

A small group of people got together in 2001 to discuss their feelings that the traditional approach to managing software development projects was failing far too often, and there had to be a better way.

They came up with the agile manifesto[1], which describes 4 important values that are as relevant today as they were then.  It says,

## Agile Manifesto

We value:

* **Individuals and interactions** over processes and tools
* **Working software** over comprehensive documentation
* **Customer collaboration** over contract negotiation
* **Responding to change** over following a plan

Though incremental practices have been in existence since late 1950’s[2], the ‘Agile Manifesto’ ushered in a new era of focus on lightweight-iterative development. The Agile Manifesto is based on twelve principles[3] :

## Agile Principles

1. Customer satisfaction by rapid delivery of useful software
2. Welcome changing requirements, even late in development
3. Working software is delivered frequently (weeks rather than months)
4. Close, daily cooperation between business people and developers
5. Projects are built around motivated individuals, who should be trusted
6. Face-to-face conversation is the best form of communication (co-location)
7. Working software is the principal measure of progress
8. Sustainable development, able to maintain a constant pace
9. Continuous attention to technical excellence and good design
10. Simplicity—the art of maximizing the amount of work not done—is essential
11. Self-organizing teams
12. Regular adaptation to changing circumstances

Agile development provides opportunities to assess the direction of the project and to evaluate the end product at very early stages. This is achieved through regular cadences of work, known as Sprints or iterations, at the end of which teams must present a potentially shippable product increment. At the beginning of every sprint, the team does a “Sprint Planning” session where it pulls requirements from the top of a “backlog”, estimates the effort and determines if they can be accomplished during the sprint or not. The requirements are in the form of “User Stories” which is a high level definition of a feature being built for an end user. We’ll talk about User Stories in detail in the next section.

## User Stories

A user story is a short, simple statement of a requirement from the perspective of the end user of a system.

It typically follows this structure :
> As a “type of user”, I want “some goal” so that “some reason”.

A user story is a very high-level definition of a requirement, containing just enough information so that the developers can produce a reasonable estimate of the effort to implement it. User stories are often written on index cards or sticky notes, stored in a shoe box, and arranged on walls or tables to facilitate planning and discussion. As such, they strongly shift the focus from writing about features to discussing them. In fact, these discussions are more important than whatever text is written.

Typically, if an index card is used, a user story might contain the following – User story summary (in the format mentioned above), priority and estimate on one side of the card and acceptance criteria on the other side.

All the user stories of a release are sorted in the order of priority in the “Release backlog”. Stories from the top of the pile are taken and a “Sprint backlog” is created for every sprint during the “Sprint Planning” meeting. At the end of every sprint, the team presents a potentially shippable product increment which is demoed during the “Sprint Review” at the end of the sprint. Details about the workflow of an Agile Sprint and related meetings would be the subject of another blog post.

## Epics

Epics are large user stories, typically ones which are too big to implement in a single iteration and therefore they need to be dis-aggregated into smaller user stories at some point. Epics are typically lower priority user stories because once the epic works its way towards the top of the work item stack.

User Stories in the backlog

<img src="/images/agile-epics.png" width="420"/>

## Conclusion

We looked at how agile methodologies took shape, what agile is, a high level overview of the development life-cycle using agile and also looked in depth into one of key artifacts of agile – “User Stories” .

# References :

* [1] Beck, Kent; et al. (2001). “Manifesto for Agile Software Development”. Agile Alliance. Retrieved 14 June 2010.
* [2] Gerald M. Weinberg, as quoted in Larman, Craig; Basili, Victor R. (June 2003). “Iterative and Incremental Development: A Brief History”.
* [3] Beck, Kent; et al. (2001). “Principles behind the Agile Manifesto”. Agile Alliance. Archived from the original on 14 June 2010. Retrieved 6 June 2010.
* [4] Ambler, S. (n.d.). User Stories: An Agile Introduction. Retrieved September 10, 2014, from http://www.agilemodeling.com/artifacts/userStory.htm
* Scott, A., & Holitza, M. (2012). Agile for Dummies. John Wiley & Sons.
* Agile Methodology. (2014, July 1). Retrieved September 10, 2014, from http://agilemethodology.org

