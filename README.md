### How do I get set up? ###

* Requirements: docker, docker-compose

* Running the automation -> Run run.sh file 


### Known issues ###
- Running only against Firefox , not using grid
- Not using cucumber/gherkin

### Problem with the story ###

1. No description what type of values should enter into fields
    1. Should be only integer or should be float (seeing the prices should be including cents) but still only integer allowed
2. Missing description of "features"
    1. the implemented solution forbidden the user to add lower price for min from the min of the product in current search
    2. actually the user can search with cents via manually set them in url
    3. if there is set this parameter currentPriceInCurrency.EUR the filter will work only for EUR for GBP will list products without this filter
3. Missing information where search should be placed
   1. Is it only in /search ? 
   2. Should be displayed if user using mobile phone? ( now it's not)
4. Different prices displaying when you have an logged user ( vat no vat...)

### Some stuff found during testing

1. When user is logged after changing the currency few times, after changing back the products staying on previous one
2. Several times it's returning 403 without any reason ( https://clippings.com/search?query=&page=%27%20or%201=1 )
3. IMO https://clippings.com/search?query=&page=  this url should go to homepageor anywhere no just blank page
4. Weird login experience , it's sending a mail with login link ...

### Test cases for min-max price

Based on my investigation seems that setting the filter is saved in local storage and its read from there
so when the language is changed then different filter will apply

Basically for this intervals seems better to use boundary values
I'm not going to write whole TC I will just write the automation one

1. Search for a product 
2. Get the price from the product
3. Set minimal (price -1) lower than price and maximum higher (price + 1) than price
4. Search again and assert that the product is visible
5. Switch the currency and repeat the steps
6. 
