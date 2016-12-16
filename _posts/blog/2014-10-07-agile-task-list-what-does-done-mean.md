---
layout: post
title:  "Agile tasks lists, what does “done” mean in Agile?"
date:   2014-10-07 21:10:13
author:     "Robinson Raju"
header-img: "img/blog4/scrum-framework2.jpg"
categories: Agile 
---

This is the fourth post in this series of “Introduction to Agile methodology”. The topic of this blog is “Agile task lists, what does “done” mean in Agile?”.

Teams change their methodology to agile with the lofty goal of getting great results but often fail. A primary reason for failure is the ambiguity around the definition of “done”. When what needs to be done in a User story is not clearly defined, what gets done does not fully meet end user requirements or even if it meets, might create technical debt. During the sprint planning, when the team discusses about the user story, everyone needs to make sure that the tasks required to complete the User Story is fully understood. If not, the scope would be inaccurate.

One way of listing down a task for the User Story is to go over a **“done thinking grid“**. A sample one is below:

<img src="/img/blog4/done-thinking-grid.png" width="420"/>


**Column 1**: Make sure that the **User Stories** for a sprint are **clear** and understood by the team. Also make sure that the acceptance criteria are validated by the product owner. Make sure that the **tasks** for the Stories have been **identified**. Estimation will not be accurate if the tasks were not clearly understood by the team. Communicate **build and package changes** to the build master if you have one. Make sure that there is enough time for the **product owner to sign off** the User Stories after the User Acceptance Test. Also ensure that the features **not done** during the sprint are **added back to the product backlog**.

**Column 2**: Make sure that development, staging and production **environment is ready** with all tools and artifacts needed to complete the tasks at hand. Continuous integration, automation, test data, etc., need to be in place. Also, the **Design** needs to be complete. Lack of design may mean that the steps in the tasks have not been thought through. This situation is risky since it could result in scope creep or not being able to deliver on time. **Unit tests, documentation and pre-**release builds need to be ready**.

**Column 3**: Make sure that all the coding for features in the task list are done. “**Code complete**” implies that coding is done, **unit testing** is done, **code re-factoring** is done, **bug fixes** are done and the code is **checked in**.

**Column 4**: Make sure that **automated code reviews**, for e.g review by a tool like P.M.D for Java coding conventions are done. Every code that is written needs to be **peer reviewed** and approved. Check if **code coverage** metrics have been maintained. If the new code didn’t add tests, coverage might decrease. Check if the project metrics like burn-down chart are updated.

**Column 5**: Ensure that the product is fully tested before being released to production. Check if **functional testing** is completed. All kinds of automated and manual testing as per test cases need to be completed. Also make sure that **Regression testing**, **Load and Performance** testing and **User Acceptance** testing are done. After this mark the tasks as closed.

**Summary**: Having one definition or checklist of “definition of done” is not practical since every project and organization is unique. Most teams go wrong with the “definition of done” in the initial stages of Agile. If the team is committed to learning from each sprint by earnestly doing Sprint retrospective, then gradually, they would get it right. Getting to a state of the ideal “definition of done” is key to delivering ship-able products that satisfy customer expectations.

# References:

* [1] Gupta, M. (2008, September 3). Definition of Done: A Reference. Retrieved November 4, 2014, from https://www.scrumalliance.org/community/articles/2008/september/definition-of-done-a-reference

* [2] Schwaber, K. (2004). Appendix A. In Agile project management with Scrum. Redmond, Wash.: Microsoft Press.


