<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>nameWindow</class>
 <widget class="QMainWindow" name="nameWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1024</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="lblBackground">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>1024</width>
      <height>600</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #ffffff;</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="scaledContents">
     <bool>true</bool>
    </property>
   </widget>
   <widget class="QLabel" name="btnHome">
    <property name="geometry">
     <rect>
      <x>-20</x>
      <y>-11</y>
      <width>201</width>
      <height>81</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>24</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 102, 0);
background-color: rgb(255, 226, 206);
border-radius:20px;</string>
    </property>
    <property name="frameShape">
     <enum>QFrame::NoFrame</enum>
    </property>
    <property name="text">
     <string>Home </string>
    </property>
    <property name="alignment">
     <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>120</x>
      <y>90</y>
      <width>781</width>
      <height>331</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: #E5E5E5;
border-radius:30px;</string>
    </property>
    <property name="frameShape">
     <enum>QFrame::NoFrame</enum>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="lblWhat">
    <property name="geometry">
     <rect>
      <x>120</x>
      <y>130</y>
      <width>781</width>
      <height>100</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>38</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>What is your name?</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QTextEdit" name="txtName">
    <property name="geometry">
     <rect>
      <x>202</x>
      <y>270</y>
      <width>621</width>
      <height>70</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>26</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">font-size: 26;</string>
    </property>
    <property name="html">
     <string>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:'MS Shell Dlg 2'; font-size:26pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLabel" name="btnScan">
    <property name="geometry">
     <rect>
      <x>387</x>
      <y>440</y>
      <width>250</width>
      <height>90</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>36</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 102, 0);
border-radius:30px;
color: #ffffff;</string>
    </property>
    <property name="frameShape">
     <enum>QFrame::Box</enum>
    </property>
    <property name="text">
     <string>Scan</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="lblHome">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>13</y>
      <width>35</width>
      <height>35</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="pixmap">
     <pixmap>images/home2.png</pixmap>
    </property>
    <property name="scaledContents">
     <bool>true</bool>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1024</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
