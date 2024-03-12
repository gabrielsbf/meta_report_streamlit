import pandas as pd
from srcs.classes.social_man import Social_Manager


def df_face_report(since, until):
    pd.set_option('display.max_colwidth', 10)
    m_sec = Social_Manager("section_m")
    m_desc = m_sec.face_description([since,until])[0]
    m_sec.merging_objects_by_id(m_desc, m_sec.face_post_metrics(m_desc),"post_id", "post_id")
    df = pd.DataFrame(m_desc).drop(columns=["post_id","message"])
    df['positive_reactions'] = df["haha"] + df['like'] + df['love'] + df['wow']
    df["negative_reactions"] = df["anger"] + df['sorry']
    df['anger'] = df["anger"] * -1
    df['sorry'] = df["sorry"] * -1
    df["engagment"] = df["shares"] + df["comments"] + df["positive_reactions"] + df["negative_reactions"]
    df["created_time"] = pd.to_datetime(df["created_time"])

    return df

