subscription={"am@gmail.com","bm@gmail.com","cm@gmail.com","dm@gmail.com"}
purchase={"bm@gmail.com","cm@gmail.com","em@gmail.com","fm@gmail.com"}

#subscribers who have not made a purchase
subscribers_only=subscription-purchase
print("Subscribers who have not made a purchase:", subscribers_only)

#purchasers who are not subscribers
purchasers_only=purchase-subscription
print("Purchasers who are not subscribers:", purchasers_only)