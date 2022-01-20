# Welcome to the bootcamp

We follow [the bootcamp agenda][agenda]. [All resources][content] will be shared after the workshop.

[agenda]: https://docs.google.com/spreadsheets/d/1gveb5v_MUqYxnMiR57YCksEHlvmXWtDsaLAdpJhcXs0/edit#gid=1068297315

[content]: https://drive.google.com/drive/folders/1zZ8N_eWWjoyV7_ypi_meCrrm7-GTn_gz

Use a provided AWS instance. For Lab 1 you can also use your local workstation.

## Intro to Lab format

This section will introduce the format for the labs used. The labs are provided as a set of milestones.

1. First, we will introduce a challenge or task for you to complete, e.g. "Task 1: Service".

1. There will be concepts and references for you to review.

1. We will timebox self-paced content during a live workshop.

1. We use [`git`][git] [branches][git-branches] to provide important milestones after a task is complete or as a starting point for a task. If you did not complete a specific task, you can use these milestones to proceed to the next task or review the solution.

1. We will wrap up the task with a group discussion / Q&A on:
    1. Why are customers doing this?
    1. What are the benefits of doing this?
    1. What are the implications?

## How to use milestones

Here is how to get to the milestone called `01service`:

=== "Shell Command"

    ```bash
    git checkout 01service
    ```

This will put you on the git branch named `01service`.

In case you have already worked on content, you might see an error like:

=== "Example Output"

    ```bash
    error: Your local changes to the following files would be overwritten by checkout:
        app.py
    Please commit your changes or stash them before you switch branches.
    Aborting
    ```

This is because your work conflicts with changes on the milestone. You have the following options:

1. If you have worked on a task and want to progress to the next one *and DROP all your changes*:

    === "Shell Command"

        ```bash
        msget 01service
        ```

    This is a shell alias to a git command we provide on the instances and identical to running:

    === "Shell Command"

        ```bash
        git reset --hard && git clean -fdx && git checkout 01service
        ```

    You will have to re-apply any local changes to files like settings tokens or names.

1. To preserve your work, but move it out of the way, you can use

    === "Shell Command"

        ```bash
        git stash && git checkout service
        ```

    To restore your work, switch to the task you were working on (e.g. `01service`) and retrieve the stashed changes:

    === "Shell Command"

        ```bash
        git checkout 01service && git stash pop
        ```

    Sometimes you run into conflicting changes with this approach. We recommend you use the first option in this case.

1. Developers use git commits to record changes and rebase or merge their work. This is not necessary for this workshop.

## How to compare (with) milestones

To compare two milestones, use

=== "Shell Command"

    ```bash
    git diff main..01service
    ```

To compare what you have with a milestone, , e.g. the milestone `01service` use

=== "Shell Command"

    ```bash
    msdiff 01service
    ```

=== "Example Output (excerpt)"

    ```bash
    ...
    diff --git a/bootcamp/service/src/app.py b/bootcamp/service/src/app.py
    index 9bcae83..b7fc141 100644
    --- a/bootcamp/service/src/app.py
    +++ b/bootcamp/service/src/app.py
    @@ -1,10 +1,12 @@
    +import json
     import re
    -from unicodedata import category
    +from flask import Flask, request, Response
    ...
    ```

[git]: https://git-scm.com/about
[git-branches]: https://backlog.com/git-tutorial/using-branches/
