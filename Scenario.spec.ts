import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
//Step 1 Visit https://useinsider.com/ and check Insider home page is opened or not
  await page.goto('https://useinsider.com/');

/*Step 2 Select “Company” menu in navigation bar, select “Careers” and check Career
page, its Locations, Teams and Life at Insider blocks are opened or not*/
  await page.getByRole('link', { name: 'Company ' }).click();
  await page.getByRole('link', { name: 'Careers' }).click();
  await expect(page.locator('#career-find-our-calling')).toBeVisible();
  await expect(page.getByText('Our Locations 25 offices across 5 continents, home to 600+ Insiders New York US')).toBeVisible();
  await expect(page.getByText('Life at Insider We’re here to')).toBeVisible();
  await page.getByRole('link', { name: 'Company ' }).click();
  await page.getByRole('link', { name: 'Careers' }).click();
  await expect(page.locator('#career-our-location')).toContainText('Our Locations');
  await page.getByRole('heading', { name: 'Life at Insider' }).click();
  await expect(page.locator('body')).toContainText('Life at Insider');
  await expect(page.locator('#career-find-our-calling')).toContainText('Find your calling');
  await expect(page.locator('#career-find-our-calling')).toContainText('See all teams');
  await expect(page.locator('#career-our-location')).toContainText('25 offices across 5 continents, home to 600+ Insiders');
  await expect(page.locator('body')).toContainText('We’re here to grow and drive growth—as none of us did before. Together, we’re building a culture that inspires us to create our life’s work—and creates a bold(er) impact. We know that we’re smarter as a group than we are alone. Become one of us if you dare to play bigger.');

/*Step 3 Go to https://useinsider.com/careers/quality-assurance/, click “See all QA
jobs”, filter jobs by Location - Istanbul, Turkey and department - Quality
Assurance, check presence of jobs list*/
  await page.goto('https://useinsider.com/careers/quality-assurance/');
  await page.getByRole('link', { name: 'See all QA jobs' }).click();
  await page.getByText('Accept All').click();
  await page.locator('#select2-filter-by-location-container').click();
  await page.locator('#select2-filter-by-location-container').click();
  await page.getByText('Istanbul, Turkey').click();
 
/*Step 4 Check that all jobs’ Position contains “Quality Assurance”, Department
contains “Quality Assurance”, Location contains “Istanbul, Turkey”*/

  await expect(page.getByText('Senior Software Quality Assurance EngineerQuality AssuranceIstanbul, TurkeyView')).toBeVisible();
  await expect(page.locator('#jobs-list')).toContainText('Quality Assurance');
  await expect(page.locator('#jobs-list')).toContainText('Istanbul, Turkey');
 
/*Step 5 . Click “View Role” button and check that this action redirects us to Lever
Application form page*/
  await page.getByText('Senior Software Quality').click();
  const page1Promise = page.waitForEvent('popup');
  await page.getByRole('link', { name: 'View Role' }).click();
  const page1 = await page1Promise;
  await expect (page1).toHaveURL('https://jobs.lever.co/useinsider/78ddbec0-16bf-4eab-b5a6-04facb993ddc');
});
