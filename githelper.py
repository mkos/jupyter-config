import git

def get_file_repo(path):
    """ Gets the Repo object having a path somewhere within a repo
        :path: path inside the repo object
        :return: initialized git.Repo object or None if _path_ is not a valid path
    """
    p = path
    while True:
        try:
            repo = git.Repo(p)
            break
        except git.exc.InvalidGitRepositoryError:
            p, x = os.path.split(p)
            continue

    return repo

def add_commit(repo, path):
    """ adds given file to commit and commits it 
        :repo: git.Repo object
        :path: path to the file to stage
    """
    repo.git.add(path)
    repo.git.commit(m='Jupyter autocommit: {}'.format(path)

def jupyter_post_save(model, path, contents_manager, **kwargs):
    repo = get_file_repo(path)
    if repo is not None:
        add_commit(repo, path)

    contents_manager.log.info('post_save succeeded')
