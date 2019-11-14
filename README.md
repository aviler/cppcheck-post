# cppcheck-post

## Description

This is an example of Platformio project setup that have cppcheck tool called everytime we run the build process. 

## References

- [Platformio Advanced Scripting](https://docs.platformio.org/en/latest/projectconf/advanced_scripting.html#advanced-scripting)

## Caution

Both AddPreAction() and AddPostAction() require a target and targets are only available for platformio.ini "post:" scripts. So only use these functions in a post build environment.
[Reference.](https://github.com/platformio/platformio-core/issues/2973#issuecomment-527423454)

[List of possible targets for the above mentioned functions.](https://docs.platformio.org/en/latest/projectconf/advanced_scripting.html#before-pre-and-after-post-actions)

## Notes

- ~~TODO FIX:The cppcheck command call is not working~~

## Changelog

0.0.1 - 