# DE-Amazon-Reviews-Project
Create an end-to-end dataflow for Amazon Reviews dataset to execute an NLP task.

## Git Convention
- Use meaningful commit messages
- Use meaningful branch names
- Always make a pull request before merging code into the `main` branch

## Get data
Use git lfs to pull the dataset from the repository.
- Set up git lfs
```bash
    git lfs install
```
- Clone repository
```bash
    git clone URL
```
### Use pointers for individual files cloning

- Set up git lfs
```bash
    git lfs install
```
- Clone without large files
```bash
    GIT_LFS_SKIP_SMUDGE=1 git clone URL
```
- Fetch large files
```bash
    git lfs fetch
```
- Replace pointers with actual data
```bash
    git lfs checkout
```