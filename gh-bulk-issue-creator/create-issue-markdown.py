# Create issue in bulk using the GitHub CLI. You would need to be in the repo folder for GitHub CLI to know which repo to create issues for.
# Heading 1 are used to get the issue titles and the content between the Heading 1's are inserted as the body of the issue.

import markdown
from bs4 import BeautifulSoup
from markdownify import markdownify
import os

# TODO: Add prompt for file path for where to create the issues from.
# TODO: Add support for adding issues to a milestone

def get_issue_data():
    html = markdown.markdown(open('test-issues.md').read())
    parsed_html = BeautifulSoup(html, 'html.parser')

    h1s = parsed_html.find_all('h1')
    issue_data = []

    for h1 in h1s:
        temp_issue_data = [h1.string]
        for tag in h1.next_siblings:
            if tag.name == 'h1':
                break
            elif tag.name:
                temp_issue_data.append(tag)

        issue_data.append(temp_issue_data)

    return issue_data

def create_issue(issue):
    title = issue[0]
    del issue[0] # Remove the title

    body = ''
    for tag in issue:
        body += f'{tag}'

    md = markdownify(body)

    os.system(f'gh issue create -t "{title}" -b "{md}"')
    print(f'{title} has been created')

def main():
    issues = get_issue_data()

    for issue in issues:
        create_issue(issue)

if __name__ == '__main__':
    main()
