class Notification:

    notification_count = 0

    def __init__(self):

        self.__notifications = []

    def send_notification(self,
                          citizen,
                          message):

        Notification.notification_count += 1

        citizen.add_notification(message)

        self.__notifications.append(
            {
                "Citizen": citizen.name,
                "Message": message
            }
        )

        print("Notification Sent")

    def broadcast(self,
                  citizens,
                  message):

        print("\nBroadcasting Notification...\n")

        for citizen in citizens:

            citizen.add_notification(message)

            self.__notifications.append(
                {
                    "Citizen": citizen.name,
                    "Message": message
                }
            )

    def total_notifications(self):

        return len(self.__notifications)

    def report(self):

        print("\n========== NOTIFICATION REPORT ==========")

        print("Total Notifications :",
              len(self.__notifications))

        print()

        for notification in self.__notifications:

            print(notification["Citizen"],
                  "->",
                  notification["Message"])