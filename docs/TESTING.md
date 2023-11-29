Return to [README.md](/README.md)  

# Testing  

## Methodology  
Throughout the development process, testing was conducted using a combination of the built-in Django debug pages were instrumental in identifying and resolving issues during the development phase, print statements were inserted into the code to check the flow and identification of potential bugs.
In addition, thorough testing has been performed and is described below, it contains of manual test to check that all user stories and acceptance criteria are met, as well as testing and validating the code with different online tools as presented below.  


### User Stories

#### Registration 
| Testing  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| User signup page | Test link is working | User is directed to the signup page | PASS |
| User signup - Form validation | Submit empty form | Form validation prompts the user | PASS |
| User signup - Form validation | Submit invalid password | Form validation prompts the user | PASS |
| User signup - Form validation | Submit non matching passwords | Form validation prompts the user | PASS |
| User login page | Test link is working | User is directed to the login page | PASS |
| User login - Form validation | Submit incorrect password | Form validation prompts the user | PASS |
| User login - Form validation | Submit incorrect name | Form validation prompts the user | PASS |
| User Logout page | Test link is working | User is logged out | PASS |

#### Home Page
| Testing | Steps | Expected Outcome| Results |
| - | - | - | - |
| Page Navigation | On the home page | The browser should display the home page with a list of the latest published blog posts | PASS |
| Latest Posts | Check if the "The Latest & Greatest" section is visible | A titled section displaying the latest blog posts should be visible at the top of the page | PASS |
| Post Display | Inspect individual post cards | Each post card should display the featured image (or a placeholder if not available), author details, publication date, title, excerpt, tags, and a "Continue reading" link | PASS |
| Author Link | Click on the author's name link | The browser should navigate to the author's profile page or sign up for a visitor| PASS |
| Post Detail Link | Click on the "Continue reading" link | The browser should navigate to the detailed view of the respective blog post | PASS |
| Pagination | Check if pagination is working | If there are more than three posts, pagination links should be visible, and clicking on them should display the next set of posts | PASS |

#### Post Detail Page
| Testing | Steps | Expected Outcome | Results |
| - | - | - | - |
| Access Page | Navigate to the post detail page for a specific post | The browser should display detailed information about the post, including title, author, creation date, featured image, tags, content, and comments | PASS |
| Tags | Check if tags are displayed correctly | Tags associated with the post should be displayed, and clicking on a tag should navigate to the tagged posts page | PASS |
| Like Post | If logged in, click the like button | The like status should toggle, and the number of likes should be updated | PASS |
| Author Profile | Check if author profile information is displayed | The post should include the author's profile image, username, bio, and a link to the author's profile page | PASS |
| Add Comment (Valid) | If logged in, enter a valid comment in the comment form and click "Send" | The comment should be posted, and a success message should be displayed | PASS |
| Add Comment (Invalid) | If logged in, enter an invalid comment (e.g., empty) and click "Send" | The comment form should not be submitted, and an error message should be displayed | PASS |
| Add Comment (Not Logged In) | If not logged in | A message should encourage the user to log in, and the comment form should not be displayed | PASS |
| Delete Comment (Own Comment) | If logged in and the comment belongs to the user, click the "Delete" button on a comment | The comment should be deleted, and a success message should be displayed | PASS |
| Edit Comment (Own Comment) | If logged in and the comment belongs to the user, click the "Edit" button on a comment, make changes, and click "Send" | The comment should be edited, and a success message should be displayed | PASS |
| Navigation | Click the "Back" link | The browser should navigate back to the home page | PASS |

#### Add Post
| Testing | Steps | Expected Outcome| Results |
| - | - | - | - |
| Access Page | Navigate to the "Add Post" page by logging in and clicking on the appropriate link  | The browser should display a form for creating a new blog post | PASS    |
| Form Fields | Inspect the form fields and labels | The form should include fields for title, content, tags, and an option to upload a featured image | PASS |
| Save Draft  | Fill in the required fields and click on the "Save Draft" button  | The form data should be saved, a success message should indicate that the post has been saved, and redirected to the draft list page | PASS |
| Publish Post | Fill in the requireded fields and click on the "Publish" button | The form data should be saved, a success message should indicate that the post is awaiting approval, and redirect to the post detail page | PASS |
| Edit Post (Authorized)| Access the "Edit Post" page for a previously saved post | The browser should display a form populated with the existing data of the selected post | PASS |
| Edit Post (Submit) | Make changes to the post data and submit the form | The post data should be updated, a success message should indicate that the post has been edited, and redirected to the post detail page | PASS |
| Delete Post (Authorized)| Access the "Delete Post" page for a previously saved post | The browser should display a confirmation prompt for deleting the post | PASS |
| Delete Post (Confirm) | Confirm the deletion of the post | The post should be deleted, and a success message should indicate that the post has been deleted | PASS |

#### Draft List 
| Testing  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| Access Page (Authorized)| Navigate to the "Draft List" page by logging in and clicking on the appropriate link | The browser should display a list of drafts if there are any, or a message encouraging the user to create a new post | PASS |
| View Drafts | If drafts are available, click on a draft link to view the draft form | The browser should display the draft form with existing data pre-filled, ready for editing | PASS |
| Edit Draft (Save Draft) | Make changes to the draft form and click on the "Save Draft" button | The changes should be saved, a success message should indicate that the draft has been saved, and redirected to the draft list page | PASS |
| Edit Draft (Publish) | Make changes to the draft form and click on the "Publish" button | The changes should be saved, the date_published field should be updated, a success message should indicate that the post is awaiting approval, and redirected to the post detail page | PASS |
| Delete Draft (Access)| Access the "Delete Draft" page for a draft | The browser should display a confirmation prompt for deleting the draft | PASS |
| Delete Draft (Confirm) | Confirm the deletion of the draft | The draft should be deleted, and a success message should indicate that the draft has been deleted | PASS |

#### Category List 
| Testing  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| Access Page | Navigate to the "Category List" page | The browser should display existing categories and an option to add a new category if the user is logged in | PASS |
| Add Category (Valid) | Enter a valid category name in the form and click on "Add Category" button | The new category should be added, and a success message should be displayed | PASS |
| Add Category (Invalid) | Enter an invalid category name (with symbols or numbers) and click on "Add Category" button | The form should not be submitted, and an error message should be displayed | PASS |
| Add Category (Unauthorized)| Attempt to add a category without being logged in | A message should encourage the user to sign up, and the form should not be displayed | PASS |
| View Category Posts | Click on an existing category link to view posts in that category | The browser should display posts associated with the selected category | PASS |
| View Empty Category Posts | Click on a category with no associated posts | A message should encourage the user to create a post in that category, and a link to create a post should be provided | PASS  |
| Back to Home | Click on the "Back" link to return to the home page | The browser should navigate back to the home page | PASS |

#### About 
| Testing  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| About Page Navigation | Click on the "About Me" link in the navigation bar  | The browser should navigate to the "About Me" page | PASS |
| Content Display | Check if the content on the "About Me" page is displayed correctly | The page  display a brief introduction about the author, including personal details and the purpose of the website | PASS |
| Sign-Up Button | Click on the "Sign Up Now!" button | The browser should navigate to the sign-up page | PASS |

#### Navbar
| Testing  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| **Home Link** | 1. Click on the "Home" link in the navbar. | Navigate to the home page. | PASS |
| **About Link** | 1. Click on the "About" link in the navbar. | Navigate to the about page. | PASS |
| **Category Link** | 1. Click on the "Category" link in the navbar. | Navigate to the category list page. | PASS |
| **Authenticated User - New Post Link** | Log in as an authenticated user. Click on the "New Post" link in the navbar. | Navigate to the page for adding a new post. | PASS |
| **Authenticated User - Profile Dropdown** | Log in as an authenticated user. Click on the profile dropdown in the navbar. | Display a dropdown with options: - Profile - Edit Profile - Your Drafts - Logout | PASS |
| **Unauthenticated User - Login Link** | Click on the "Login" link in the navbar. | Navigate to the login page. | PASS |
| **Unauthenticated User - Sign Up Link** |  Click on the "Sign Up" link in the navbar. | Navigate to the sign-up page. | PASS |
| **Search Bar** | 1. Enter a search query in the search bar. Click on the search button. | Navigate to the search results page with relevant search results. | PASS |
| Toggle Nav Bar | The navigation bar should collapse into a toggle button | Click the toggle button in the collapsed navigation bar | PASS |

#### Search Bar Results Page
| Testing  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| **Search Results - Posts Found** | Enter a search query in the search bar. Click on the search button. | Display a list of posts that match the search query. Each post should show: - Featured image (or a default image if no image is available) - Number of likes - Title - Excerpt - Tags | PASS |
| **Search Results - No Posts Found** | Enter a search query that has no matching posts. Click on the search button. | Display a message stating "NO POSTS FOUND. TRY A DIFFERENT SEARCH?" along with a list of most common tags. | PASS |
| **No Search Query Entered** | Visit the search results page without entering a search query. | Display a message stating "Oops! You Forgot To Search For A Recipe...! Use the search bar at the top" along with a list of most common tags. | PASS |

#### Tags Page
| Testing  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| **Display Tagged Posts** |  Should display the tag page for a specific tag. | Display a list of posts that are tagged with the selected tag. Each post should show: - Featured image (or a default image if no image is available) - Number of likes - Title - Excerpt - Tags | PASS |
| **Display Most Common Tags** | Visit any tag page. | Display a section showing the most common tags, each clickable to navigate to the respective tag page. | PASS |



#### Admin
| Testing  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| Admin login - Form validation | Submit incorrect password | Form validation prompts the user | PASS |
| Admin login - Form validation | Submit incorrect name | Form validation prompts the user | PASS |
| Admin login - Form validation | Submit incorrect name | Form validation prompts the user | PASS |
| Admin panel | Owner is able to update posts | Post is updated | PASS |
| Admin panel | Owner is able to approve user's posts | Post-s users is published | PASS |
| Admin panel | Owner is able to delete posts | Post is deleted from current post list | PASS |

<br/>

Return to [README.md](/README.md)