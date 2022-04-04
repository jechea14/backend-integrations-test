# backend-integrations-test

## Approach
- Split problem into steps, split steps into smaller steps, repeat
- Work on the data cleaning of the two csv files first then work on the api
- Lots of research
- Data cleaning:
  - Experiment with the data in a jupyter notebook to vizualize dataframes
  - Read the csv files into two separate dataframes
  - Filter and clean data
  - Organize into functions
  - Write Unit tests for the functions
- Api:
  - Use Docker config files to get Docker running for the environment variables
  - Use Postman for the requests
  - Write unit tests for the api routes

## Learned
- More about Pandas, apis, and unit testing
- Regex
- Practice more on splitting the problem into smaller steps
- Problem solving
- How to Research a lot
- Git: Work on a separate branch then make a pull request. Trying not to commit to main

## Challenges Encountered
- Reading csv into dataframes with a | delimiter (solved)
- Using regex to filter out the package (solved)
- Could not get Docker-compose to work on MacOS machine, dependency issues (solved by using a Windows machine)
  - Could not get any of the environment variables without running Docker-compose on MacOS
  - Kept getting jinja2 errors in my python3.7 folder which does not exist in my MacOS machine
- Having trouble passing Unit tests for the products and update_merchant routes as I've been getting a 400 code
  - 3/5 test cases passed though!
- Could not figure out how to automatically inject data straight into the api as a POST request
  - However, I was able to successfully make a POST request with the required body manually
  - Maybe format data into json to match with the json_schema then loop through each row of data while making one POST request at a time (?)

## Future Improvements
- Figure out how to pass the unit tests for the products and update_merchant routes
- Automate injecting data into the api

## Final Thoughts
- I had a lot of fun working on this take home test!
- I am willing to learn more and improve my skills
- Feedback is always appreciated