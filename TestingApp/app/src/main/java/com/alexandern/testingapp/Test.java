package com.alexandern.testingapp;

import android.app.Activity;
import android.widget.Button;
import android.content.DialogInterface;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

/**
 * Created by AlexanderN on 6/16/2015.
 */
public class Test extends Activity {
    Button myButton;

    public void NewScreen(){
        myButton = (Button) findViewById(R.id.button);
    }
}
