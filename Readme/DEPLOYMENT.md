

<h3 align="center" style="color:skyblue">IMPORTANT THINGS</h3>



- Atfist get <b>Telegram APP ID or API ID</b> And <b> APP HASH or API HASH</b> from [Here](https://my.telegram.org/auth?to=apps)



- Get a <b>Bot Token</b> from [Here](https://telegram.me/BotFather)



- Obtain a <b>MongoDB connection string</b> from [MongoDB Atlas](https://www.mongodb.com/cloud/atlas). If you're unsure how to create one, you can search for tutorials('how to make a mongodb connection string') on YouTube or ask for help in our support group at [Hb Support](https://t.me/hbbotz_supportch). Ensure that you've configured the IP whitelist to allow connections from anywhere (0.0.0.0/0).



<hr>



# Deployment Steps



<details>

<summary>For VPS</summary>

<p>

<pre>

git clone https://github.com/TeamHMT/Auto-search-tamil-bot

# Install Packages

pip3 install -U -r requirements.txt

Edit info.py with variables as given below then run bot

python3 bot.py

</pre>

</p>

</details>



<b style="color:skyblue">**Now Your Bot Is Ready 🔥**</b>



</details>



<details>

<summary>For Koyeb Or Render</summary>



### Deploying this bot in Render is Almost same as deploying it in Koyeb. You Just need to Follow the Steps.

<p>

<pre>

- Fork the Repo And Import it in Koyeb or Render By Choosing Web Services.

- Choose Dockerfile if any Server Asks For it.

- For Koyeb In Builder Section Choose Dockerfile option.

- If you are using koyeb then add port 8000 or 8080

- Add All Env Variables In Environment Variables Section.

</pre>

</p>

### Now Your Bot Is Ready To Deploy🔥



</details>



<details>

<summary>For Heroku</summary>

<p>

<pre>

- Create A new app in Heroku.

- Import the forked repo.

- Deploy it.

- Add all Env Variables in app settings in Heroku.

- Check Resources if the dyno is on or off. If off, then turn it on.

</pre>

</p>

### Now Your Bot Is Ready In Heroku Server🔥



</details>
