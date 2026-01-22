class Book:
    def __init__(self,title,author,reviews):
        self.title=title
        self.author=author
        self.reviews=reviews
    def addReview(self,review):
        self.reviews.append(review)
        print("review added successfully")
    def countReviews(self):
        print(f"No of reviews:{len(self.reviews)}")
    def display(self):
        for review in self.reviews:
            print(review)
b1=Book("Discipline","Shyam",["easy going","good starter"])
b1.display()
b1.addReview("hello from Py oop")
b1.display()