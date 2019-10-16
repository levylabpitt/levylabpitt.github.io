# Host Your Own VIPM Repository on GitHub

Host your VI Package Manager repository on GitHub

1. Follow the instructions [here](https://pages.github.com/) to create a site on GitHub.
The repository must have the name [username].github.io in order to work.

![](screenshots/create_repo.png)

2. Create a new file in your repository called "index.html". Commit your new file. You can then view your site by visiting "[username].github.io" in about 10 minutes.

![](screenshots/create_index.png)

3. In the meantime, setup VI Package Manager. Clone your newly created git repository by running "git clone"

![](screenshots/clone_ssh.png)

![](screenshots/git_clone.png)

4. In VI Package Manager open Tools >> Options >> Repository Manager

![](screenshots/VIPM_repo_manager.png)

5. Click the "+" sign to browse for your [username].github.io repository folder. Give your repository a name.

![](screenshots/VIPM_browse.png)

![](screenshots/VIPM_repo_setup.png)

6. While you are still in the VIPM >> Options window, go to the Network Tab of VIPM and subscribe to https://[username].github.io

![](screenshots/VIPM_subscribe/png)

7. VIPM will not find any packages yet because you did not yet synchronize with the GitHub server. Before you do that add a package by going through the Repository Manager.

![](screenshots/VIPM_publish.png)

![](screenshots/VIPM_repo_manager_2.png)

8. Git Commit and Synchronize your repository to GitHub.

![](screenshots/git_commit.png)

9. Check for new changes in the VIPM repository
