# No-Cheating-App

The No Cheating App serves as a companion application to the Examination Management System. Its purpose is to prevent cheating during exams.

The app opens in full-screen mode, restricting students from accessing any applications or websites besides the exam. It also disables specific keys on the keyboard to prevent unauthorized actions. 


1)	Full-Screen Mode: The app opens in full-screen mode, preventing students from accessing any applications or websites other than the exam. This restriction ensures that students stay focused on the exam and eliminates potential distractions.

2)	Key Disabling: The app disables Window key on the keyboard that are not required during the exam. With this key (window+R), the student can open any file in the system like pdf and PowerPoint by cmd.

We didn’t prevent any other keys such as Ctrl, Alt, and Delete because the student may want to use, for example, Ctrl+C to copy, and Ctrl+V to paste. But if he tries to open any app such as whatsApp  with these keys, the app prevents showing it because the No Cheating App will open on top of any other apps.

# The implementation of No Cheating App:

•	The No Cheating App was developed using Python.

•	We used QtWebEngineWidgets module in the PyQt5 library that provides a set of classes for embedding web content in PyQt applications. It allows you to integrate web-based components and functionality into your PyQt applications.

•	We used a QWebEngineView class of the PyQt5.QtWebEngineWidgets module. It is a widget that provides a web browsing view and enables the rendering and display of web content within a PyQt application.

•	We used keyboard module to block keys during the app.


