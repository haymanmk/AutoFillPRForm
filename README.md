# :lollipop:AutoFillPRForm

This project aims to build an autonomous program to address the tedious work on filling purchase request form belonging to our company.

## :wrench:Prerequisites

Before diving into the technical part,  there are few tools needed to be install beforehand.

* python3
* selenium package
* chromedriver_autoinstaller
* (optional) XPath selector extension for chrome
* (optional) visual studio code IDE
* (optional) Git

In addition, the knowledge of **XPath** and basic **python programming skills** are also required here.



## :bug:What is Selenium?

"***Selenium automates browsers. That's it!***", quote from [Selenium](https://www.selenium.dev/) website. In order to automate the tedious work on filling the PR (in short of Purchase Request) form, this project implements Selenium to search for target elements, like input boxes, drop list, buttons, etc., in the PR form and commit actions on them to mimic how people work on it.



## :mag:What is XPath?

[XPath](https://www.guru99.com/xpath-selenium.html) ***in Selenium*** *is an XML path used for navigation through the HTML structure of the page.* In a nutshell, XPath is a syntax or semantic for finding elements on the a web page.

The basic format of XPath is as shown below.

```xml
XPath=//Tagname[@Attribute='value']
```

* **'//'** indicates it is a **Relative XPath** which means no need to write a long path, **Absolute XPath**, with entire tags starting from ancestor tags down to the  target tag. **Relative XPath** can squarely search  for the target element without knowing the entire ancestor tags of this element.

  Here is the example Relative versus Absolute XPath.

  ``````python
  # Absolute XPath
  XPath = /html/body/div[2]/div[1]/div/h4[1]/b/html[1]/body[1]/div[2]/div[1]/div[1]/h4[1]/b[1]
  
  # Relative XPath
  XPath = //b[1]
  ``````

  And it is quite obvious to see the differences between the length of each path. Relative XPath has a shortest path comparing to Absolute.

* **'Tagname'** stands for the tag in html which can be found in the **DevTool** of web browser. In general, press **F12** to launch DevTool in browser. For more detailed about html, refer to [W3Schools](https://www.w3schools.com/) web site.

* **@Attribute** specifies the attribute belonging to target tag, like class, id, text, etc.  The detailed explanation for these attributes can be found in [W3Schools](https://www.w3schools.com/) as well.

* **'value'** is the target value of the attribute. And it is supposed to be single-quoted.



## :construction_worker:Troubleshooting

### :x:WebDriver' object has no attribute 'find_element_by_id' or so

Selenium just removed `find_element_by_*` and `find_elements_by_*` in version `4.3.0`. If you get an error like '''WebDriver' object has no attribute 'find_element_by_id' or so, it means your Selenium is in version 4.3.0 now.

#### Solution

Update the Selenium to latest version.



### :x:Element not visible/found

* Element is not yet generated.
* Element is still in below the fold.

Some contents shown on the **web page might update dynamically** at run time which means these could take time to generate or even send request to backend and wait for the response. 

Besides, some web page would introduce the **'Above the Fold'** technique to improve the response latency when browser is loading the web page. This technique considers the contents which will be seen immediately  by users as top priority. And these high priority contents will be passed to client first. The rest of the contents below the above the fold, so called **Below the Fold**, would be **temporarily invisible** and should turn into visible when users scroll the page down which will further triggering download action for the hidden contents.

#### Solution

To address this issue, the Selenium WebDriver provides few functions to wait for the target element loaded, and  DOM API supports scrolling page down to the visible part.

* [WebDriverWait](https://www.learncodewithmike.com/2020/06/python-selenium-waits.html)
* [scrollIntoView](https://stackoverflow.com/questions/70896097/how-to-scroll-element-selenium-python)
