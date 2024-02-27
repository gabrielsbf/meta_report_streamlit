import pandas as pd
from srcs.classes.social_man import Social_Manager


def print_df(since, until):
    m_sec = Social_Manager("section_m")
    m_desc = m_sec.face_description([since,until])[0]
    m_sec.merging_objects_by_id(m_desc, m_sec.face_post_metrics(m_desc),"post_id", "post_id")
    df = pd.DataFrame(m_desc)
    print(df)
