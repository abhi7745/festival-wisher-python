from datetime import date, datetime

# print(date.today())
current_year = date.today()
# print(current_year.year)

import smtplib
import ssl
from email.message import EmailMessage

# for normal use ---------------------------------------------
from config import SENDER_EMAIL, PASSWORD, RECEIVER_EMAIL_DICT
# for normal use ---------------------------------------------

# for github action case start-------------------
# from config import RECEIVER_EMAIL_DICT
# import os
# SENDER_EMAIL = os.environ['SENDER_EMAIL']
# PASSWORD = os.environ['PASSWORD']
# for github action case end--------------------

# christmas email sender function and template - start
def christmas_email_sender(receiver_name, festival_name):
    # message setting area
    message=EmailMessage()
    message['From'] = SENDER_EMAIL
    message['To'] = receiver_name
    message['Subject'] = festival_name
    # message.set_content(body)


    html = f"""
    <!DOCTYPE html>

<head>
	<title></title>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings></xml><![endif]-->
	<!--[if !mso]><!-->
	<link href="https://fonts.googleapis.com/css?family=Abril+Fatface" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Droid+Serif" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Oswald" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Roboto+Slab" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Merriweather" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Oxygen" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Permanent+Marker" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Nunito" rel="stylesheet" type="text/css">

</head>

<body style="background-color: #FFFFFF; margin: 0; padding: 0; -webkit-text-size-adjust: none; text-size-adjust: none;">
	<table class="nl-container" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #FFFFFF;">
		<tbody>
			<tr>
				<td>
					<table class="row row-1" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #f7f5f2;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-image: url('https://d1oco4z2z1fhwp.cloudfront.net/templates/default/696/christmas4_1.gif'); background-position: top center; background-repeat: no-repeat; color: #000000; width: 640px;" width="640">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 0px; padding-bottom: 0px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="divider_block block-1" width="100%" border="0" cellpadding="20" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad">
																<div class="alignment" align="center">
																	<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
																		<tr>
																			<td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 0px solid #BBBBBB;"><span>&#8202;</span></td>
																		</tr>
																	</table>
																</div>
															</td>
														</tr>
													</table>
													<table class="text_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-bottom:25px;padding-left:10px;padding-right:10px;padding-top:10px;">
																<div style="font-family: Arial, sans-serif">
																	<div class style="font-size: 14px; font-family: 'Roboto Slab', Arial, 'Helvetica Neue', Helvetica, sans-serif; mso-line-height-alt: 16.8px; color: #555555; line-height: 1.2;">
																		<p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 16.8px;"><span style="color:#ffffff;"><span style="font-size:18px;">· December<span style="color:#c4b384;"><strong><span style> 25th</span></strong></span> ·</span><br></span></p>
																	</div>
																</div>
															</td>
														</tr>
													</table>
													<table class="image_block block-3" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="width:100%;padding-right:0px;padding-left:0px;">
																<div class="alignment" align="center" style="line-height:10px"><img class="big" src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/696/309fddd6-3e45-4125-a490-d88dbcde5939.png" style="display: block; height: auto; border: 0; width: 384px; max-width: 100%;" width="384" alt="Image" title="Image"></div>
															</td>
														</tr>
													</table>
													<table class="image_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="width:100%;padding-right:0px;padding-left:0px;">
																<div class="alignment" align="center" style="line-height:10px"><img class="big" src="https://freepngimg.com/save/19109-santa-claus-png-hd/336x359" style="display: block; height: auto; border: 0; width: 416px; max-width: 100%;" width="416" alt="Image" title="Image"></div>
															</td>
														</tr>
													</table>
													<table class="divider_block block-5" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-bottom:30px;padding-left:25px;padding-right:25px;padding-top:25px;">
																<div class="alignment" align="center">
																	<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
																		<tr>
																			<td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 0px solid #BBBBBB;"><span>&#8202;</span></td>
																		</tr>
																	</table>
																</div>
															</td>
														</tr>
													</table>
													<table class="text_block block-6" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-bottom:5px;padding-left:15px;padding-right:15px;padding-top:15px;">
																<div style="font-family: Tahoma, Verdana, sans-serif">
																	<div class style="font-size: 14px; font-family: 'Roboto', Tahoma, Verdana, Segoe, sans-serif; mso-line-height-alt: 21px; color: #555555; line-height: 1.5;">
																		<p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 21px;"><span style><span style="color:#333300;">By</span></span></p>
																		<p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 21px;"><span style><span style="color:#333300;">Abhijith KR</span></span></p>
																	</div>
																</div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-2" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #f7f5f2;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 640px;" width="640">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="divider_block block-1" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad">
																<div class="alignment" align="center">
																	<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
																		<tr>
																			<td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 0px solid #BBBBBB;"><span>&#8202;</span></td>
																		</tr>
																	</table>
																</div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					
				</td>
			</tr>
		</tbody>
	</table><!-- End -->
</body>

</html>

    """

    message.add_alternative(html, subtype="html")
    context=ssl.create_default_context() # it securing connection

    print(f'Sending Email to {receiver_name}')

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(SENDER_EMAIL, PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_name, message.as_string())

    print(f'{festival_name} wish sended to ', receiver_name)
# christmas email sender function and template - end   

# newyear email sender function and template - start
def newyear_email_sender(receiver_name, festival_name):
    # message setting area
    message=EmailMessage()
    message['From'] = SENDER_EMAIL
    message['To'] = receiver_name
    message['Subject'] = festival_name
    # message.set_content(body)


    html = f"""
	<!DOCTYPE html>
	<html xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en">

	<head>
		<title></title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet" type="text/css">
		<link href="https://fonts.googleapis.com/css?family=Permanent+Marker" rel="stylesheet" type="text/css">
		<link href="https://fonts.googleapis.com/css?family=Roboto+Slab" rel="stylesheet" type="text/css">
	</head>

	<body style="background-color: #000000; margin: 0; padding: 0; -webkit-text-size-adjust: none; text-size-adjust: none;">
		<table class="nl-container" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #000000;">
			<tbody>
				<tr>
					<td>
						<table class="row row-1" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-image: url('https://d1oco4z2z1fhwp.cloudfront.net/templates/default/186/ezgif-4-4ffef0a72c0c.gif'); background-position: top center; background-repeat: no-repeat;">
							<tbody>
								<tr>
									<td>
										<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 650px;width: 100% !important;" width="650">
											<tbody>
												<tr>
													<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 0px; padding-bottom: 0px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
														<table class="divider_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
															<tr>
																<td class="pad" style="padding-left:10px;padding-right:10px;padding-top:10px;">
																	<div class="alignment" align="center">
																		<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="20%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
																			<tr>
																				<td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 2px dotted #E92C41;"><span>&#8202;</span></td>
																			</tr>
																		</table>
																	</div>
																</td>
															</tr>
														</table>
														<div class="spacer_block mobile_hide" style="height:30px;line-height:30px;font-size:1px;">&#8202;</div>
														<table class="text_block block-3" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
															<tr>
																<td class="pad" style="padding-top:20px;">
																	<div style="font-family: sans-serif">
																		<div class style="font-family: 'Permanent Marker', Impact, Charcoal, sans-serif; font-size: 12px; mso-line-height-alt: 14.399999999999999px; color: #E92C41; line-height: 1.2;">
																			<p style="margin: 0; text-align: center; font-size: 12px; mso-line-height-alt: 14.399999999999999px;"><span style="font-size:64px;">Happy</span></p>
																			<p style="margin: 0; text-align: center; font-size: 12px; mso-line-height-alt: 14.399999999999999px;"><span style="font-size:64px;">NEW YEAR</span></p>
																		</div>
																	</div>
																</td>
															</tr>
														</table>
														<table class="text_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
															<tr>
																<td class="pad">
																	<div style="font-family: Arial, sans-serif">
																		<div class style="font-family: 'Roboto Slab', Arial, 'Helvetica Neue', Helvetica, sans-serif; font-size: 12px; mso-line-height-alt: 14.399999999999999px; color: #FFFFFF; line-height: 1.2;">
																			<p style="margin: 0; text-align: center; font-size: 12px; mso-line-height-alt: 14.399999999999999px;"><span style="font-size:80px;"><strong><span style>{current_year.year+1}</span></strong></span></p>
																		</div>
																	</div>
																</td>
															</tr>
														</table>
													</td>
												</tr>
											</tbody>
										</table>
									</td>
								</tr>
							</tbody>
						</table>
						<table class="row row-2" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #FFFFFF; background-image: url('https://d1oco4z2z1fhwp.cloudfront.net/templates/default/186/fireworksbg_1.jpg'); background-position: top center; background-repeat: repeat;background-size: 1114px 370px;">
							<tbody>
								<tr>
									<td>
										<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 650px;width: 100% !important;" width="650">
											<tbody>
												<tr>
													<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
														<table class="text_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
															<tr>
																<td class="pad" style="padding-bottom:10px;padding-left:10px;padding-right:10px;padding-top:300px;">
																	<div style="font-family: sans-serif">
																		<div class style="font-size: 12px; mso-line-height-alt: 18px; color: #000000; font-weight: bold; line-height: 1.5; font-family: Lato, Tahoma, Verdana, Segoe, sans-serif;">
																			<p style="margin: 0; font-size: 12px; text-align: center; mso-line-height-alt: 18px;">By</p>
																			<p style="margin: 0; font-size: 12px; text-align: center; mso-line-height-alt: 18px;">Abhijith KR</p>
																		</div>
																	</div>
																</td>
															</tr>
														</table>
													</td>
												</tr>
											</tbody>
										</table>
									</td>
								</tr>
							</tbody>
						</table>
						
					</td>
				</tr>
			</tbody>
		</table><!-- End -->
	</body>

	</html>
    """

    message.add_alternative(html, subtype="html")
    context=ssl.create_default_context() # it securing connection

    print(f'Sending Email to {receiver_name}')

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(SENDER_EMAIL, PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_name, message.as_string())

    print(f'{festival_name} wish sended to ', receiver_name)
# newyear email sender function and template - end 

# republic-day email sender function and template - start
def republic_day_email_sender(receiver_name, festival_name):
    # message setting area
    message=EmailMessage()
    message['From'] = SENDER_EMAIL
    message['To'] = receiver_name
    message['Subject'] = festival_name
    # message.set_content(body)


    html = f"""
        <!DOCTYPE html>
<html xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en">

<head>
	<title></title>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings></xml><![endif]-->
	<!--[if !mso]><!-->
	<link href="https://fonts.googleapis.com/css?family=Bitter" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Shrikhand" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Permanent+Marker" rel="stylesheet" type="text/css">
	<link href="https://fonts.googleapis.com/css?family=Oswald" rel="stylesheet" type="text/css">
	<!--<![endif]-->
	
</head>

<body style="background-color: #071013; margin: 0; padding: 0; -webkit-text-size-adjust: none; text-size-adjust: none;">
	<table class="nl-container" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #071013;">
		<tbody>
			<tr>
				<td>
					<table class="row row-1" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #f6d8df;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 680px;" width="680">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="image_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="width:100%;padding-right:0px;padding-left:0px;">
																<div class="alignment" align="center" style="line-height:10px"><img class="fullMobileWidth" src="https://file.pngbackground.com/uploads/preview/happy-republic-day-cb-editing-background-11609963695kdtfsaxgvm.jpg" style="display: block; height: auto; border: 0; width: 680px; max-width: 100%;" width="680"></div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-2" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 680px;" width="680">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="text_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-left:20px;padding-right:20px;padding-top:10px;">
																<div style="font-family: sans-serif">
																	<div class style="font-size: 12px; mso-line-height-alt: 14.399999999999999px; color: #a9a9a9; line-height: 1.2; font-family: Bitter, Georgia, Times, Times New Roman, serif;">
																		<p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 16.8px;"><a href="http://www.example.com" target="_blank" style="text-decoration: none; color: #ffffff;" rel="noopener"></a>By</p>
																		<p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 16.8px;">Abhijith KR</p>
																	</div>
																</div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
				</td>
			</tr>
		</tbody>
	</table><!-- End -->
</body>

</html>
    """

    message.add_alternative(html, subtype="html")
    context=ssl.create_default_context() # it securing connection

    print(f'Sending Email to {receiver_name}')

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(SENDER_EMAIL, PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_name, message.as_string())

    print(f'{festival_name} wish sended to ', receiver_name)
# republic-day email sender function and template - end

# independence day email sender function and template - start
def independence_day_email_sender(receiver_name, festival_name):
    # message setting area
    message=EmailMessage()
    message['From'] = SENDER_EMAIL
    message['To'] = receiver_name
    message['Subject'] = festival_name
    # message.set_content(body)


    html = f"""
	<!DOCTYPE html>
	<html xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en">

	<head>
		<title></title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0"><!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings></xml><![endif]--><!--[if !mso]><!--><!--<![endif]-->
	</head>

	<body style="text-size-adjust: none; background-color: #eee; margin: 0; padding: 0;">
		<table class="nl-container" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #eee;">
			<tbody>
				<tr>
					<td>
						<table class="row row-1" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
							<tbody>
								<tr>
									<td>
										<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000; background-color: #f9d075; background-position: top; width: 640px; margin: 0 auto;" width="640">
											<tbody>
												<tr>
													<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; font-weight: 400; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
														<div class="spacer_block block-1" style="height:60px;line-height:60px;font-size:1px;">&#8202;</div>
														<table class="image_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
															<tr>
																<td class="pad" style="width:100%;padding-right:0px;padding-left:0px;">
																	<div class="alignment" align="center" style="line-height:10px"><img class="fullWidth" src="https://pngfreepic.com/wp-content/uploads/2021/08/independence-day-png-94.png?v=1663321175" style="height: auto; display: block; border: 0; max-width: 640px; width: 100%;" width="640" alt="Independence Day Banner Image" title="Independence Day Banner Image"></div>
																</td>
															</tr>
														</table>
														<div class="spacer_block block-3" style="height:60px;line-height:60px;font-size:1px;">&#8202;</div>
													</td>
												</tr>
											</tbody>
										</table>
									</td>
								</tr>
							</tbody>
						</table>
						<table class="row row-2" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
							<tbody>
								<tr>
									<td>
										<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000; background-color: #fff; width: 640px; margin: 0 auto;" width="640">
											<tbody>
												<tr>
													<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; font-weight: 400; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
														<table class="text_block block-1" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
															<tr>
																<td class="pad">
																	<div style="font-family: Arial, sans-serif">
																		<div class style="font-size: 12px; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; mso-line-height-alt: 14.399999999999999px; color: #c0c0c0; line-height: 1.2;">
																			<p style="margin: 0; font-size: 12px; text-align: center; mso-line-height-alt: 14.399999999999999px;"><span style="color:#152a6d;"><span style="font-size:14px;">By</span></span></p>
																			<p style="margin: 0; font-size: 12px; text-align: center; mso-line-height-alt: 14.399999999999999px;"><span style="color:#152a6d;"><span style="font-size:14px;">Abhijith KR</span></span></p>
																		</div>
																	</div>
																</td>
															</tr>
														</table>
													</td>
												</tr>
											</tbody>
										</table>
									</td>
								</tr>
							</tbody>
						</table>
						
					</td>
				</tr>
			</tbody>
		</table><!-- End -->
	</body>

	</html>

    """

    message.add_alternative(html, subtype="html")
    context=ssl.create_default_context() # it securing connection

    print(f'Sending Email to {receiver_name}')

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(SENDER_EMAIL, PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_name, message.as_string())

    print(f'{festival_name} wish sended to ', receiver_name)
# independence day email sender function and template - end

# Gandhijayanti email sender function and template - start
def gandhijayanthi_email_sender(receiver_name, festival_name):
    # message setting area
    message=EmailMessage()
    message['From'] = SENDER_EMAIL
    message['To'] = receiver_name
    message['Subject'] = festival_name
    # message.set_content(body)


    html = f"""
		<!DOCTYPE html>
		<html xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en">

		<head>
			<title></title>
			<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
			<meta name="viewport" content="width=device-width, initial-scale=1.0"><!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings></xml><![endif]--><!--[if !mso]><!-->
			<link href="https://fonts.googleapis.com/css?family=Bitter" rel="stylesheet" type="text/css"><!--<![endif]-->
		</head>

		<body style="background-color: #071013; margin: 0; padding: 0; -webkit-text-size-adjust: none; text-size-adjust: none;">
			<table class="nl-container" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #071013;">
				<tbody>
					<tr>
						<td>
							<table class="row row-1" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #f6d8df;">
								<tbody>
									<tr>
										<td>
											<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000; width: 680px; margin: 0 auto;" width="680">
												<tbody>
													<tr>
														<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
															<table class="image_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
																<tr>
																	<td class="pad" style="width:100%;padding-right:0px;padding-left:0px;">
																		<div class="alignment" align="center" style="line-height:10px"><img class="fullWidth" src="https://4f6d41cc50.imgdist.com/public/users/Integrators/BeeProAgency/877412_861586/editor_images/5-Happy-Gandhi-Jayanti-2022_1.jpg" style="display: block; height: auto; border: 0; max-width: 680px; width: 100%;" width="680"></div>
																	</td>
																</tr>
															</table>
														</td>
													</tr>
												</tbody>
											</table>
										</td>
									</tr>
								</tbody>
							</table>
							<table class="row row-2" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
								<tbody>
									<tr>
										<td>
											<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000; width: 680px; margin: 0 auto;" width="680">
												<tbody>
													<tr>
														<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
															<table class="text_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
																<tr>
																	<td class="pad" style="padding-bottom:10px;padding-left:20px;padding-right:20px;padding-top:10px;">
																		<div style="font-family: sans-serif">
																			<div class style="font-size: 12px; font-family: Bitter, Georgia, Times, Times New Roman, serif; mso-line-height-alt: 14.399999999999999px; color: #a9a9a9; line-height: 1.2;">
																				<p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 16.8px;"><a href="http://www.example.com" target="_blank" style="text-decoration: none; color: #ffffff;" rel="noopener"></a>By</p>
																				<p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 16.8px;">Abhijith KR</p>
																			</div>
																		</div>
																	</td>
																</tr>
															</table>
														</td>
													</tr>
												</tbody>
											</table>
										</td>
									</tr>
								</tbody>
							</table>
							
						</td>
					</tr>
				</tbody>
			</table><!-- End -->
		</body>

		</html>
    """

    message.add_alternative(html, subtype="html")
    context=ssl.create_default_context() # it securing connection

    print(f'Sending Email to {receiver_name}')

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(SENDER_EMAIL, PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_name, message.as_string())

    print(f'{festival_name} wish sended to ', receiver_name)
# Gandhijayanti email sender function and template - end


# main area to check whether the festival fount - start

# Keep in mind that the cron job is set to run at UTC time, specifically at 6:30 PM UTC, which corresponds to 12:00 AM Indian Time on the following day. 
# example:
	# The requirement is to run the script at 12:00 AM on October 2, 2023, in India. However, due to the UTC time difference, 
	# the script actually runs at 6:30 PM UTC on October 1, 2023. As a result, the festival dates are set one day before the actual date in Indian time. 
	# In other words, it runs the script on UTC date 2023-10-01 6:30 PM while in India, it corresponds to midnight 12:00 AM on 2023-10-02.
fest_name_data = {
                    'NewYear' : f'{current_year.year}-12-31', # NewYear: 2023-01-01
                    'RepublicDay' : f'{current_year.year}-01-25', # RepublicDay: 2023-01-26
                    'IndependenceDay' : f'{current_year.year}-08-14', # IndependenceDay: 2023-08-15
                    'GandhiJayanti' : f'{current_year.year}-10-01',  # GandhiJayanti: 2023-10-02
                    'Christmas' : f'{current_year.year}-12-24', # Christmas: 2022-12-25
                }

for fest_name, day in fest_name_data.items():
    # print(fest_name, day)
    if date.today() == datetime.strptime(day, '%Y-%m-%d').date():
        # print('Trueee')
        if fest_name == 'NewYear':
            print('NewYear', day)
            for receiver_name in RECEIVER_EMAIL_DICT:
                # print(receiver_name)
                newyear_email_sender(receiver_name, 'Happy New Year!')

        elif fest_name == 'RepublicDay':
            print('RepublicDay', day)
            for receiver_name in RECEIVER_EMAIL_DICT:
                # print(receiver_name)
                republic_day_email_sender(receiver_name, 'Happy Republic!')

        elif fest_name == 'IndependenceDay':
            print('IndependenceDay', day)
            for receiver_name in RECEIVER_EMAIL_DICT:
                # print(receiver_name)
                independence_day_email_sender(receiver_name, 'Happy Independence!')

        elif fest_name == 'GandhiJayanti':
            print('GandhiJayanti', day)
            for receiver_name in RECEIVER_EMAIL_DICT:
				# print(receiver_name)
                gandhijayanthi_email_sender(receiver_name, 'Happy Gandhi Jayanti!')

        elif fest_name == 'Christmas':
            print('Christmas', day)
            for receiver_name in RECEIVER_EMAIL_DICT:
                # print(receiver_name)
                christmas_email_sender(receiver_name, 'Happy Christmas!')

    # else:
    #     print('No festival found on the date : ', date.today())


print('Completed.........!')