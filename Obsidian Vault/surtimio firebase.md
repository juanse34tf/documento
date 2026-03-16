import 'package:firebase_core/firebase_core.dart';
import 'firebase_options.dart';

// ...

await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
); 
-- All done!
surtimio-41099102:~/myapp$ dart pub global activate flutterfire_cli 
The Dart CLI developer tool uses Google Analytics to report usage and diagnostic
data along with package dependencies, and crash reporting to send basic crash
reports. This data is used to help improve the Dart platform, Flutter framework,
and related tools.

Telemetry is not sent on the very first run. To disable reporting of telemetry,
run this terminal command:

    dart --disable-analytics

If you opt out of telemetry, an opt-out event will be sent, and then no further
information will be sent. This data is collected in accordance with the Google
Privacy Policy (https://policies.google.com/privacy).

Package flutterfire_cli is currently active at version 1.2.0.
Downloading packages... . (1.3s)
The package flutterfire_cli is already activated at newest available version.
To recompile executables, first run `dart pub global deactivate flutterfire_cli`.
Installed executable flutterfire.
Activated flutterfire_cli 1.2.0.
surtimio-41099102:~/myapp$ flutterfire configure --project=surtmio-rebuild 
i Found 0 Firebase projects.                                                                   
Failed to fetch your Firebase projects. Fetch failed with this: TimeoutException after 0:00:40.000000: Future not completed
✔ Would you like to create a new Firebase project? · yes                                       
✔ Enter a project id for your new Firebase project (e.g. my-cool-project) · surtimio           
⠋ Creating new Firebase project surtimio...                                                    
FirebaseCommandException: An error occured on the Firebase CLI when attempting to run a command.
COMMAND: firebase projects:create surtimio --json 
ERROR: Failed to create project because there is already a project with ID surtimio. Please try again with a unique project ID.
surtimio-41099102:~/myapp$ flutterfire configure --project=surtmio-rebuild 
i Found 6 Firebase projects. Selecting project surtmio-rebuild.                                
✔ Which platforms should your configuration support (use arrow keys & space to select)? · android, web 
i Firebase android app com.example.myapp is not registered on Firebase project surtmio-rebuild.
i Registered a new Firebase android app on Firebase project surtmio-rebuild.                   
i Firebase web app myapp (web) is not registered on Firebase project surtmio-rebuild.          
i Registered a new Firebase web app on Firebase project surtmio-rebuild.                       

Firebase configuration file lib/firebase_options.dart generated successfully with the following Firebase apps:

Platform  Firebase App Id
web       1:1063349088201:web:867c91adf5d2d5c7004218
android   1:1063349088201:android:e122455d6f611afe004218

Learn more about using this file and next steps from the documentation:
 > https://firebase.google.com/docs/flutter/setup
surtimio-41099102:~/myapp$  


Learn more about using this file and next steps from the documentation:
 > https://firebase.google.com/docs/flutter/setup
surtimio-41099102:~/myapp$ flutter pub add firebase_core && flutter pub add firebase_ai 
"firebase_core" is already in "dependencies". Will try to update the constraint.
Resolving dependencies... 
Downloading packages... 
  flutter_lints 5.0.0 (6.0.0 available)
  leak_tracker 10.0.9 (11.0.1 available)
  leak_tracker_flutter_testing 3.0.9 (3.0.10 available)
  leak_tracker_testing 3.0.1 (3.0.2 available)
  lints 5.1.1 (6.0.0 available)
  material_color_utilities 0.11.1 (0.13.0 available)
  meta 1.16.0 (1.17.0 available)
  test_api 0.7.4 (0.7.6 available)
  vector_math 2.1.4 (2.2.0 available)
  vm_service 15.0.0 (15.0.2 available)
Got dependencies!
10 packages have newer versions incompatible with dependency constraints.
Try `flutter pub outdated` for more information.
Resolving dependencies... 
Downloading packages... 
+ _flutterfire_internals 1.3.56
+ crypto 3.0.6
+ firebase_ai 2.1.0
+ firebase_app_check 0.3.2+7
+ firebase_app_check_platform_interface 0.1.1+7
+ firebase_app_check_web 0.2.0+11
+ firebase_auth 5.6.0
+ firebase_auth_platform_interface 7.7.0
+ firebase_auth_web 5.15.0
  flutter_lints 5.0.0 (6.0.0 available)
+ http 1.4.0
+ http_parser 4.1.2
  leak_tracker 10.0.9 (11.0.1 available)
  leak_tracker_flutter_testing 3.0.9 (3.0.10 available)
  leak_tracker_testing 3.0.1 (3.0.2 available)
  lints 5.1.1 (6.0.0 available)
  material_color_utilities 0.11.1 (0.13.0 available)
  meta 1.16.0 (1.17.0 available)
  test_api 0.7.4 (0.7.6 available)
+ typed_data 1.4.0
  vector_math 2.1.4 (2.2.0 available)
  vm_service 15.0.0 (15.0.2 available)
+ web_socket 1.0.1
+ web_socket_channel 3.0.3
Changed 14 dependencies!
10 packages have newer versions incompatible with dependency constraints.
Try `flutter pub outdated` for more information.