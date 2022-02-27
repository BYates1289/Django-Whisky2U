<h1><strong>Whisky2U</strong></h1>
<br>
<h1>Product Description</h1>
<p>My Milestone 4 project for the Code Institute, is a Full Stack Whisky E-commerce site, where users can purchase rare whiskies from around the globe either as a one off or by subscribing to monthly deliveries.</p>
<p>The project has been deployed to Heroku and can been seen <a href="https://whisky-project-ms4.herokuapp.com/">here.</a></p>
<h1>Table of Contents</h1>
<ul>
    <li><a href="#user-experience">User Experience (UX)</a></li>
    <ul>
        <li><a href="#user-stories">User Stories</a></li>
    </ul>
    <li><a href="#design">Design</a></li>
    <ul>
        <li><a href="#colour-scheme">Colour Scheme</a></li>
        <li><a href="#typography">Typography</a></li>
        <li><a href="#imagery">Imagery</a></li>
        <li><a href="#wireframes">Wireframes</a></li>
    </ul>
    <li><a href="#features">Features</a></li>
    <li><a href="#technologies-used">Technologies Used</a></li>
    <li><a href="#frameworks">Frameworks Used</a></li>
    <li><a href="#dbschema">Database Schema</a></li>
    <li><a href="#testing">Testing</a></li>
        <ul>
            <li><a href="#code-verification">Code Verification</a></li>
            <li><a href="#speed-test">Speed Test</a></li>
            <li><a href="#cross-browser">Cross-Browser</a></li>
            <li><a href="#responsive">Responsive Testing</a></li>
            <li><a href="#testing-user-stories">Testing User Stories</a></li>
        </ul>
    <li><a href="#further-testing">Further Testing</a></li>
    <li><a href="#features-to-implement">Features Left To Implement</a></li>
    <li><a href="#bugs">Bugs</a></li>
    <li><a href="#deployment">Deployment</a></li>
        <ul>
            <li><a href="#heroku">Heroku</a></li>
            <li><a href="#forking-repo">Forking the GitHub Repository</a></li>
            <li><a href="#making-local-clone">Making a Local Clone</a></li>
        </ul>
    <li><a href="#credits">Credits</a></li>
    <li><a href="#code">Code</a></li>
    <li><a href="#content">Content</a></li>
    <li><a href="#media">Media</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
</ul>

<h2 id="user-experience">User Experience (UX)</h2>
<ul>
    <li id="user-stories">User Stories</li>
        <ul>
            <li id="ft-visitor">First Time Visitor Goals</li>
                <ol type="a">
                    <li>As a First Time Visitor, I want to see the range of whiskies on sale.</li>
                    <li>As a First Time Visitor, I want to read reviews from fellows members about their experience.</li>
                    <li>As a First Time Visitor, I want to find out more about the subscription option.</li>
                </ol>
            <li id="returning-visitor">Returning Visitor Goals</li>
                <ol type="a">
                    <li>As a Returning Visitor, I want to see if there are more whiskies available.</li>
                    <li>As a Returning Visitor, I want to see which whisky is recommended this month.</li>
                    <li>As a Returning Visitor, I want to see which whiskies are being rated the highest.</li>
                </ol>                       
        </ul>
    <li id="design">Design</li>
        <ul>
            <li id="colour-scheme">Colour Scheme</li>
                <ul>
                    <li>The colour scheme is largly black, white and orange with a few other pastel colours, which I feel compliment the site quite well.</li>                         
                </ul>
            <li id ="typography">Typography</li>
                <ul>
                    <li>The Raleway font is the main font used throughout this project with Sans-Serif as the fallback in case for any reason the font isn't being imported into the site correctly.</li>
                </ul>
            <li id="imagery">Imagery</li>
                <ul>
                    <li>Alot of the images have been designed by a friend of mine who works in Graphic Design. Other images include bottles of whisky, which have been sourced from an online whisky retailer.</li>
                </ul>
            <li id="wireframes">Wireframe</li>
                <ul>
                    <li>Project Wireframe - <a href="#">View</a></li>
                </ul>
            </li>
        </ul>
    <li id="target-audience">Target Audience</li>
        <ul>
            <li>Users aged 18 years or older.</li>
            <li>Whisky veterans.</li>
            <li>People who may not have tried whisky before.</li>
        </ul>
    </li>
</ul>
<h2 id="features">Features</h2>
<ul>
    <li>Responsive on all device sizes.</li>
    <li>Interactivity carousels.</li>
    <li>Users can make one off purchases.</li>
    <li>Users can set up a monthly subscription to recieve their favourite whisky on a monthly basis.</li>
    <li>Users can leave reviews and rate whiskies they have purchased.</li>
    <li>Users can update their address from their account page</li>
    <li>Users can track all their previous purchases.</li>
    <li>Users can cancel their monthly subscription from their account page</li>
</ul>
<h2 id="technologies-used">Technologies Used</h2>
<h3>Languages Used</h3>
<ul>
    <li>HTML5</li>
    <li>CSS3</li>
    <li>JavaScript</li>
    <li>Python</li>
</ul>
<h3 id="frameworks">Frameworks, Libraries & Programs Used</h3>
<ol>
    <li><a href="https://getbootstrap.com/docs/5.1/getting-started/introduction/">Bootstrap 5</a></li>
        <ul>
            <li>Bootstrap was used to assist with the responsiveness and styling of the website.</li>
        </ul>
    <li><a href="https://www.djangoproject.com/">Django</a></li>
        <ul>
            <li>Backend Python micro-framework.</li>
        </ul>
    <li><a href="https://www.heroku.com/postgres">PostgreSQL</a></li>
        <ul>
            <li>Open source object-relational database that is used to store data.</li>
        </ul>
    <li><a href="https://fonts.google.com/">Google Fonts</a></li>
        <ul>
            <li>Google Fonts was used to import the 'Raleway' font into my project.</li>
        </ul>
    <li><a href="https://fontawesome.com/">Font Awesome</a></li>
        <ul>
            <li>Font Awesome was used for icons in this project.</li>
        </ul>
    <li><a href="https://jquery.com/">jQuery</a></li>
        <ul>
            <li>jQuery is a dependency of the Bootstrap framework and helps with responsive design.</li>
        </ul>
    <li><a href="https://owlcarousel2.github.io/OwlCarousel2/">Owl-Carousel</a></li>
        <ul>
            <li>Used to create a touch enabled, responsive carousel slider.</li>
        </ul>
    <li><a href="https://code.visualstudio.com/">VS Code</a></li>
        <ul>
            <li>The Code Editor used for this project.</li>
        </ul>
    <li><a href="https://git-scm.com/">Git</a></li>
        <ul>
            <li>Git was used for version control.</li>  
        </ul>
    <li><a href="https://github.com/">GitHub</a></li>
        <ul>
            <li>GitHub is used to store the projects code after being pushed from Git.</li>
        </ul>
    <li><a href="https://desktop.github.com/">GitHub Desktop</a></li>
        <ul>
            <li>Used to commit and push changes to GitHub.</li>
        </ul>
    <li><a href="https://balsamiq.com/">Balsamiq</a></li>
        <ul>
            <li>Balsamiq was used to create the wireframes during the design process.</li>
        </ul>
    <li><a href="https://developer.chrome.com/docs/devtools/">Chrome DevTools</a></li>
        <ul>
            <li>Essential tools for debugging code.</li>
        </ul>
</ol>

<h2 id="testing">Testing</h2>
<h3 id="code-verification">Code Verification</h3>
<p>JavaScript and Python code was put through a validator to ensure of no errors.</p>
<ul>
    <li>JSHint - <a href="https://github.com/BYates1289/Whisky-Project-MS4/blob/main/static/new_static/images/testing/JSHint.pdf">Results</a></li>
    <li>Python Validator - Code was formatted by the <a href="https://marketplace.visualstudio.com/items?itemName=himanoa.Python-autopep8">autopep8</a> VSCode extension.</li>
</ul>
<h3 id="speed-test">Speed Test</h3>
<p>Site speed test was performed by <a href="https://gtmetrix.com/">GTMetrix</a>. Here are the results.</p>
<img src="https://github.com/BYates1289/Whisky-Project-MS4/blob/main/static/new_static/images/testing/GTMetrix.png">
<p>A full report can be viewed <a href="https://github.com/BYates1289/Whisky-Project-MS4/blob/main/static/new_static/images/testing/GTmetrix%20Performance%20Report.pdf">here</a>.</p>
<h3 id="cross-browser">Cross Browser Testing</h3>
<p>This project was tested with all major browsers and displayed as expected. Results can be seen here.</p>
<ul>
    <li><a href="https://github.com/BYates1289/Whisky-Project-MS4/blob/main/static/new_static/images/testing/Chrome.pdf">Google Chrome</a></li>
    <li><a href="https://github.com/BYates1289/Whisky-Project-MS4/blob/main/static/new_static/images/testing/Firefox.pdf">Firefox</a></li>
    <li><a href="https://github.com/BYates1289/Whisky-Project-MS4/blob/main/static/new_static/images/testing/Safari.png">Safari</a></li>
    <li><a href="https://github.com/BYates1289/Whisky-Project-MS4/blob/main/static/new_static/images/testing/Opera.pdf">Opera</a></li>
    <li><a href="https://github.com/BYates1289/Whisky-Project-MS4/blob/main/static/new_static/images/testing/Edge.pdf">Microsoft Edge</a></li>
</ul>
<h3 id="responsive">Responsive Testing</h3>
<p>Responsive testing was carried out with Chrome Dev Tools. The results for some popular devices can be seen below.</p>
<ul>
    <li><a href="https://github.com/BYates1289/Whisky-Project-MS4/blob/main/static/new_static/images/testing/whisky-project-ms4.herokuapp.com_(Galaxy%20Fold).png">Galaxy Fold</a>(280px)</li>
    <li><a href="https://github.com/BYates1289/Whisky-Project-MS4/blob/main/static/new_static/images/testing/whisky-project-ms4.herokuapp.com_(iPhone%20SE).png">iPhone SE</a>(320px)</li>
    <li><a href="https://github.com/BYates1289/Whisky-Project-MS4/blob/main/static/new_static/images/testing/whisky-project-ms4.herokuapp.com_(iPhone%20X).png">iPhone X</a>(375px)</li>  
    <li><a href="https://github.com/BYates1289/Whisky-Project-MS4/blob/main/static/new_static/images/testing/whisky-project-ms4.herokuapp.com_(Pixel%202%20XL).png">Pixel 2 XL</a>(411px)</li>
    <li><a href="https://github.com/BYates1289/Whisky-Project-MS4/blob/main/static/new_static/images/testing/whisky-project-ms4.herokuapp.com_(Surface%20Duo).png">Surface Duo</a>(540px)</li>
    <li><a href="https://github.com/BYates1289/Whisky-Project-MS4/blob/main/static/new_static/images/testing/whisky-project-ms4.herokuapp.com_(iPad).png">iPad</a>(768px)</li>
    <li><a href="https://github.com/BYates1289/Whisky-Project-MS4/blob/main/static/new_static/images/testing/whisky-project-ms4.herokuapp.com_(iPad%20Pro).png">iPad Pro</a>(1024px)</li>   
</ul>
<h3 id="testing-user-stories">Testing User Stories from User Experience (UX) Section</h3>
<ul>
    <li>First Time Visitor Goals</li>
        <ol type="I">
            <li>As a First Time Visitor, I want to see the range of whiskies on sale.</li>
                <ol type="a">
                    <li>Upon entering the Shop section of the site, users are presented with the entire whisky stock available to order. Users can use the filter options to filter how much they wish to spend, age of the whisky and bottle sizes.</li>
                </ol>
            <li>As a First Time Visitor, I want to read reviews from fellows members about their experience.</li>
                <ol type="a">
                    <li>Each product has a review section. Underneath the product description is where you will find written reviews based on the experiences of fellow memebers.</li>
                    <li>Once a product has been purchased, the user can leave a rating out of 5, which will display next to the price.</li>
                </ol>
            <li>As a First Time Visitor, I want to find out more about the subscription option.</li>
                <ol type="a">
                    <li>Every product has the option for you to either Buy Now as a one off or Subscribe, which will set up a monthly reoccuring payment in which you will recieve a regular delivery of your favourite whisky.</li>
                </ol>            
        </ol>
    <li>Returning Visitor Goals</li>
        <ol type="I">
            <li>As a Returning Visitor, I want to see if there are more whiskies available.</li>
                <ol type="a">
                    <li>Users can find the entire stock range in the Shop section. Newly aquired whiskies are also displayed in the Latest Arrivals section on the Home page.</li>
                </ol>
            <li>As a Returning Visitor, I want to see which whisky is recommended this month.</li>
                <ol type="a">
                    <li>Each month we will display our recommend whisky of the month. You will find this on the Home page.</li>
                </ol>
            <li>As a Returning Visitor, I want to see which whiskies are being rated the highest.</li>
                <ol type="a">
                    <li>Each month we will display our most popular whisky of the month. You will find this on the Home page.</li>
                    <li>Every product can be rated by a user who has purchased that product. They can leave a rating out of 5. This can be found alongside the price of the product. If multiple users leave a different rating the site will work out an average.
                </ol>                        
        </ol>
</ul>
<h3 id="further-testing">Further Testing</h3>
<ul>
    <li>The application was personally tested on a variety of devices such as Desktop, Laptop, Surface Pro 6, iPad Air 2 & iPhone X.</li>
    <li>All testing was undertaken offline using VS Code in a Python Virtual Environment (venv).</li>
    <li>Family members and friends were asked to navigate the application and leave a review. Everyone who tested, confirmed the site was simple to navigate.</li>
</ul>
<h3 id="features-to-implement">Features Left To Implement</h3>
<ul>
    <li>I want to integrate a subscription model where users can get different whisky brand each month. Currently, users only get the same whisky which they subscribed to.</li>
    <li>I think the site would benefit from pagination. Throughtout testing, I only had a few products listed and didn't think of this at the time. This was an oversight by myself.</li>
</ul>
<h2 id="bugs">Bugs</h2>
<strike>If a user purchased a product, which is then marked as delivered by admin. If they then subscribe to the same product on a monthly basis, it is automatically marked as delivered after checkout.</strike>
<h2 id="deployment">Deployment</h2>
<h3 id="heroku">Heroku</h3>
<p>To deploy this project to Heroku, the following steps were taken...</p>
<ol>
    <li>From the VS Code terminal, I created a requirements.txt and Procfile using the following commands:</li><br>
    <div class="snippet-clipboard-content position-relative"><pre><code>pip3 freeze --local > requirements.txt</pre></code></div>
    <div class="snippet-clipboard-content position-relative"><pre><code>echo web: python run.py > Procfile</pre></code></div>
    <li>I then committed these files to GitHub.</li>
    <li>Next, I logged into my Heroku account and created a new app named "whisky-project-ms4".</li>
    <li>I then located the <b>Deploy</b> tab and selected <b>GitHub</b> as the Deployment Method.</li>
    <li>Once I authenticated my GitHub account, I selected my repository.</li>
    <li>Then, I went to <b>Settings</b> and clicked the <b>Reveal Config Vars</b> button.</li>
    <li>Next, I went back to the <b>Deploy</b> tab and selected <b>Enable Automatic Deploys</b>.</li>
    <li>I then ensured the "main" branch was selected under Manual Deploy, and clicked the <b>Deploy Branch</b> button.</li>
    <li>Shortly after, I recieved a message informing me that my site had been deployed sucessfully.</li>
</ol>
<h3 id="forking-repo">Forking the GitHub Repository</h3>
<p>By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...</p>
<ol>
    <li>Log in to GitHub and locate the GitHub Repository.</li>
    <li>At the top of the Repository, just above the "Settings" Button on the menu, locate the "Fork" Button.</li>
    <li>You should now have a copy of the original repository in your GitHub account.</li>
</ol>
<h3 id="making-local-clone">Making a Local Clone</h3>
<ol>
    <li>Log in to GitHub and locate the GitHub Repository.</li>
    <li>Under the repository name, click "Clone or download"</li>
    <li>To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.</li>
    <li>Open Git Bash.</li>
    <li>Change the current working directory to the location where you want the cloned directory to be made.</li>
    <li>Type <code>git clone</code>, and then paste the URL you copied in Step 3.</li><br>
    <div class="snippet-clipboard-content position-relative"><pre><code>$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY</pre></code></div>
    <li>Press Enter. Your local clone will be created.</li><br>
    <div class="snippet-clipboard-content position-relative">    
    <pre><code>$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY    
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.</pre></code></div>
</ol>
<p>Click <a href="https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository#cloning-a-repository-to-github-desktop">here</a> to retrieve pictures for some of the buttons and more detailed explanations of the above process.</p>
<h2 id="credits">Credits</h2>
<h3 id="code">Code</h3>
<ul>
    <li>Bootstrap 5: Bootstrap Library used throughout the project to make site responsive.</li>
    <li>Owl-Carousel for the touch enabled, responsive carousel.</li>
    <li>My friend, Lewis, for the site graphics</li>
</ul>
<h3 id="content">Content</h3>
<ul>
    <li>All content was written by the developer over a period of 3 months.</li>
</ul>
<h3 id="media">Media</h3>
<ul>
    <li>The Logo was designed on <a href="https://www.freelogodesign.org/">https://www.freelogodesign.org/</a></li>
    <li>The product images were downloaded from <a href="https://www.oldandrarewhisky.co.uk/">https://www.oldandrarewhisky.co.uk/</a></li>
</ul>
<h3 id="acknowledgements">Acknowledgements</h3>
<ul>
    <li>My work colleagues at <a href="https://www.sgworld.com/">SG World</a>, for their insightful feedback/pointers and also for my paid subscription to <a href="https://www.pluralsight.com/">Pluralsight</a>.
    <li><a href="https://codeinstitute.net/">Code Institute</a>, <a href="https://www.pluralsight.com/">Pluralsight</a>, <a href="https://www.udemy.com/">Udemy</a> and <a href="https://youtube.com">YouTube</a> for their extremely good course materials.</li>
    <li>The wonderfully helpful <a href="https://codeinstitute.net/">Code Institute</a> Slack community.</li>
    <li>My partner and children for putting up with the constant headaches throughout this project and allowing me to study in peace when the world around us was in a state of chaos.</li>
</ul>