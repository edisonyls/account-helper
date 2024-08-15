import instaloader

bot = instaloader.Instaloader()
username = "YOUR_INSTAGRAM_USERNAME"
password = "YOUR_INSTAGRAM_PASSWORD"
bot.login(username, password)

profile = instaloader.Profile.from_username(bot.context, 'PERSON_YOU_WANT_TO_CHECK')

followers = [follower.username for follower in profile.get_followers()]

followings = [followee.username for followee in profile.get_followees()]

not_following_back = set(followings) - set(followers)

print("Users you follow but do not follow you back:")
for user in not_following_back:
    print(user)
