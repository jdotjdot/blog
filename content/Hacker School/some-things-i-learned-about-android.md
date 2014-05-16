Title: Some things I learned about Android
Date: 2014-03-24
Slug: some-things-i-learned-about-android
Category: Programming
Tags: hackerschool, android, java
Status: published



###Activity layouts: XML vs Java
For a long while, I couldn't really understand the difference between the XML files and the Java files.   It seemed at first like the XML files determine what objects are available on the display for a particular activity, and then the actions and interactivity of those objects are determined by an accompanying Java file.  However, when working later with another android developer example, I saw that the buttons were actually being created *in Java* and not included in the XML at all:

    :::java
	@Override
	protected void onCreate(Bundle icicle) {
		super.onCreate(icicle);
		
		LinearLayout ll = new LinearLayout(this);
		mRecordButton = new RecordButton(this);
		ll.addView(mRecordButton,
				new LinearLayout.LayoutParams(
						ViewGroup.LayoutParams.WRAP_CONTENT,
						ViewGroup.LayoutParams.WRAP_CONTENT,
						0));
		mPlayButton = new PlayButton(this);
		ll.addView(mPlayButton,
				new LinearLayout.LayoutParams(
						ViewGroup.LayoutParams.WRAP_CONTENT,
						ViewGroup.LayoutParams.WRAP_CONTENT,
						0));
				
		setContentView(ll);
		
		//super.onCreate(icicle);
		//setContentView(R.layout.activity_audio_record_test);
	}
    
The commented out block at the bottom is what appears by default when creating the activity using the GUI in Android Developer Tools.  I realized that the `R.layout.activity_audio_record_test` corresponsed to the filepath `res/layout/activity_audio_record_test.xml`, which was the auto-generated layout XML file.  But the reason none of that was making its way to the actual app was because the `setContentView` function that would call it is commented out, and instead there is a `setContentView(ll)` above that uses an Android `LinearLayout` object created entirley in Java.

To compare, in XML, this would probably look something like the following:

    :::xml
    <LinearLayout xlmns:android=“http://schemas.android.com/apk/res/android”
        xlmns:tools=“http://schemas.android.com/tools”
        android:layout_width=“match_parent”
        android:layout_height=“match_parent”
        android:paddingBottom="@dimen/activity_vertical_margin"
        android:paddingLeft="@dimen/activity_horizontal_margin"
        android:paddingRight="@dimen/activity_horizontal_margin"
        android:paddingTop="@dimen/activity_vertical_margin"
        tools:context=“.AudioRecordTest” >
    
        <Button 
            android:layout_width=“wrap_content”
            android:layout_height=“wrap_content”
            android:text=“Start Recording”
            android:Id=“@+id/record_button”
            android:onClick=“onRecord” />
    
        <Button
            android:layout_width=“wrap_content”
            android:layout_height=“wrap_content”
            android:text=“Start Playing”
            android:Id=“@+id/play_button”
            android:onClick=“onPlay” />
    
    </LinearLayout>

Much uglier, in my opinion.


