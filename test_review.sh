# .github/workflows/test-review.yml
name: Review Generated Tests
on:
  workflow_run:
    workflows: ["Test Generation and Mutation Analysis"]
    types:
      - completed

jobs:
  review-tests:
    runs-on: ubuntu-latest
    if: ${{ github.event.workflow_run.conclusion == 'success' }}
    steps:
    - uses: actions/checkout@v3
    
    - name: Download generated tests
      uses: actions/github-script@v6
      with:
        script: |
          const artifacts = await github.rest.actions.listWorkflowRunArtifacts({
            owner: context.repo.owner,
            repo: context.repo.repo,
            run_id: ${{ github.event.workflow_run.id }}
          });
          const matchArtifact = artifacts.data.artifacts.find(artifact => 
            artifact.name === "generated-tests"
          );
          const download = await github.rest.actions.downloadArtifact({
            owner: context.repo.owner,
            repo: context.repo.repo,
            artifact_id: matchArtifact.id,
            archive_format: 'zip'
          });
          require('fs').writeFileSync('generated-tests.zip', Buffer.from(download.data));
    
    - name: Extract generated tests
      run: |
        unzip generated-tests.zip -d ./download
        mkdir -p ./tests/ci_generated
        cp ./download/* ./tests/ci_generated/
    
    - name: Run tests and check coverage
      run: |
        pytest ./tests/ci_generated/ --cov=your_module --cov-report=xml
    
    - name: Create or update pull request
      uses: peter-evans/create-pull-request@v4
      with:
        token: ${{ secrets.GITHUB_TOKEN }}
        commit-message: "Add CI-generated tests"
        title: "CI: Generated Tests Update"
        body: |
          This PR contains automatically generated tests from Pynguin.
          
          Please review the tests for:
          - Correctness
          - Edge cases
          - Test naming and organization
          
          Tests may need modification before merging.
        branch: ci-generated-tests
        path: ./tests/ci_generated/