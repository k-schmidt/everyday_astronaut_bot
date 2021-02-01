from dataclasses import dataclass, fields

from html_utils.HtmlParser import HtmlParser


class Launch:

    launch_video_url = "https://youtube.com/everydayastronaut/live"

    @dataclass
    class LaunchInfo:
        time: str
        mission_name: str
        launch_provider: str
        customer: str
        rocket: str
        launch_location: str
        payload_mass: str
        destination: str
        first_stage_recovery: str
        first_stage_recovery_location: str
        fairings_recovery_locations: str
        are_fairings_new: str
        weather: str
        extra_data: str
        video_url: str

    def __init__(self, article_website):
        self.article_website = article_website
        self.launch_info = article_website

    @property
    def launch_info(self):
        return self.__launch_info

    @launch_info.setter
    def launch_info(self, article_website):
        article_soup = HtmlParser.get_html_and_load(article_website)
        table_rows = article_soup.find_all("tr")
        launch_info_dict = {
            key: tr.td.get_text() if key != 'video_url' else self.launch_video_url
            for key, tr in zip(self.get_launch_info_keys(), table_rows)
        }
        self.__launch_info = self.LaunchInfo(**launch_info_dict)

    def get_launch_info_keys(self):
        return [f.name for f in fields(self.LaunchInfo)]

    def form_message(self):
        return "\n".join(
            [
                "Mission: " + self.launch_info.mission_name,
                "Time: " + self.launch_info.time,
                "Rocket: " + self.launch_info.launch_provider + " " + self.launch_info.rocket,
                self.launch_info.video_url
            ]
        )
