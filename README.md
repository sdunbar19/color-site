Simple color analyzer written with Django and React.

To run locally -> from base directory
- run "pipenv shell", if on a new machine run "pipenv install -r requirements.txt"
- cd backend, run "python manage.py runserver"
- in a separate terminal, cd frontend, run "yarn start"
- navigate to localhost:3000, the site should load there

To use -> 
- Upload an image to get the kmeans distribution, scaled by number of pixels in the clusters
    - Image file name cannot be more than 100 chars
    - Only PNG and JPG
- Click the cells of the kmeans to get the hex values and h/s/v values (all out of 255)
- To see color distribution, enter the h/s/v values of a color (natural numbers out of 255 each)
    - In order L->R, schemes are -> 
        - 2 adjacent analagous, closer and further
        - Analagous scheme and the complementary color swatch x5
            - Original, and the four variants of saturation/value changes with opposite change in complementary
        - Triangular colors
        - Saturation/value variation x 2 (low/low to high/high, and low/high to high/low)
        - Hue variation with saturation/value variation x 4
        - One sided adjacent/complementary x 10
            - Hue shift left x 5, hue shift right x 5
            - Original and saturation/value variation x 4 each
        - Complementary range x 5, original and saturation/value variations
- This will show various splits of colors, which you can also click on to get hex and h/s/v values
