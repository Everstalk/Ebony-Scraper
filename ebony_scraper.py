import requests
from bs4 import BeautifulSoup

link = 'https://www.ebonystory.com/story/returned/episode-'
number_of_episodes = 13
directory = "/Users/michaelsaneke/Desktop/Scraper/output/episode-"

# Functionality for scraping the story from the page
def story_scraper(link, c):
    episode_response = requests.get(link)
    episode_data = episode_response.content

    soup = BeautifulSoup(episode_data, 'html.parser')

    # 'story-body'class is where the story we want to scrape is located 
    whole_episode = soup.find_all("div", class_="story-body")

    paragraphs = ""

    # Get <h1> and <p> tags under the <div> tag with class="story-body"
    for episode in whole_episode:
        title_element = episode.find("h1")
        story_element = episode.find_all("p")
        
        # Second loop if the body of the story is contained in multiple <p> tags
        for p in story_element :
            paragraphs += '\n' + p.text

        f = open(directory + str(c)+".txt", "w")
        f.write(title_element.text)
        f.write(str(paragraphs))
    

# Method to scrape each page given the number of episodes in the story
def full_scrape(number_of_episodes):
    c = 1
    for i in range(1, number_of_episodes + 1):
        story_scraper(link + str(i), c)
        c += 1


full_scrape(number_of_episodes)
