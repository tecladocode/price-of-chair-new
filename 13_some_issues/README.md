# Some issues?

At this point in our application, we've got a few things that are excellent.

We know what we want the application to _do_, and that is sometimes the hardest thing.

We've built the application incrementally, so that over time we have added new features. We've learned from this, and now we would be able to add more features with relative ease.

However there are some clear issues. For starters, it's impossible to create alerts since after we create an item, we don't know the `item_id` so we can't give it to the alert form.

This application up to now is something that happens very often when developers begin building an application. There is initially little consideration for the user and the usability of the application. We like to build forms and buttons that add data to a database and manipulate it, but we haven't yet stopped to think how the users will want to use the application.

To begin thinking about this, we must think about what users are coming to our application for. I can guarantee you, they're not coming to add items and alerts.

They want to get something from our application, and our job is to give them that as simply and quickly as possible.

I'd venture to say what users want from this application is to tell us the item they want, and for what price they want it. The rest is up to us.

We should not require users to fill in two forms in order to achieve this. We should not expect users to give us the HTML tag and query every time they want to create a new item. We should certainly not require users to know our internal database IDs in order to create new alerts!

---

I think in this application, the users are interested in alerts. For that reason, I think we will not need users to be able to create items and then create alerts. Users should create alerts, and we should handle the item creation on the background.

However, we do need to know about the HTML tag and query in order to be able to find the item price...

By introducing the concept of Stores, I think we can manage this. All items in an online store will likely have the same HTML tag and query, so by creating a single store (e.g. for John Lewis), we could then know if the item is part of that store by looking at the Item's URL and comparing it with the Store URL. If they match, we can know that the Item's HTML tag and query are the same as the store's HTML tag and query—and this means we only have to add them in once.