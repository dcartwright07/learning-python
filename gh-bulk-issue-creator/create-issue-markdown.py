import markdown
from bs4 import BeautifulSoup
from markdownify import markdownify
import os


def get_issue_data(filename):
    with open(filename) as file:
        html = markdown.markdown(file.read())

    parsed_html = BeautifulSoup(html, 'html.parser')

    h1s = parsed_html.find_all('h1')
    issue_data = []

    for h1 in h1s:
        temp_issue_data = [h1.string]
        for tag in h1.next_siblings:
            if tag.name == 'h1':
                break
            elif tag.name == 'h6':
                temp_issue_data.insert(1, tag.string)
            elif tag.name:
                temp_issue_data.append(tag)

        issue_data.append(temp_issue_data)

    return issue_data


def create_issue(issue):
    title, milestone, *issue = issue

    body = ''
    for tag in issue:
        body += f'{tag}'

    md = markdownify(body)

    os.system(f'gh issue create -t "{title}" -b "{md}" -m "{milestone}"')
    print(f'{title} has been created')


def main():
    filename = input("Which file do you want to use?")
    issues = get_issue_data(filename)

    for issue in issues:
        create_issue(issue)


if __name__ == '__main__':
    main()
